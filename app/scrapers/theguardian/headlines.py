import datetime
import scrapy

TODAY = datetime.datetime.now()

class TGHeadlinesSpider(scrapy.Spider):
    name = 'tg-headlines'
    allowed_domains = ['theguardian.com']

    def __init__(self, *args, **kwargs):
        super(TGHeadlinesSpider, self).__init__(*args, **kwargs)
        date = getattr(self, 'date', False)

        if len(kwargs) <= 1 and not date:
            self.start_urls = ['https://www.theguardian.com/environment']

        else:
            if date :
                # Runned with : scrapy runspider headlines.py -a date=2020-03-27
                # Runned with : scrapy runspider headlines.py -a date=YYYY-MM-DD
                date = datetime.datetime.strptime(date, "%Y-%m-%d")

            else:
                # Runned with : scrapy runspider headlines.py -a year=2020 -a month=2 -a day=2
                # Runned with : scrapy runspider headlines.py -a year=2020 -a month=2 -a day=16
                date = datetime.datetime(
                    int(getattr(self, 'year', TODAY.year)),
                    int(getattr(self, 'month', TODAY.month)),
                    int(getattr(self, 'day', TODAY.day))
                )

            self.start_urls = [f'https://www.theguardian.com/environment/{date.strftime("%Y")}/{date.strftime("%b").lower()}/{date.strftime("%d")}/all']

    def parse(self, response):
        articles = response.css(".fc-item__container")  # Extract the articles
        for article in articles:  # Loop over the articles
            title = article.xpath('a/text()').extract()
            link = article.xpath('a/@href').extract()
            tag = article.xpath('.//span[@class="fc-item__kicker"]/text()').extract()
            image = article.xpath('.//source/@srcset').extract_first()

            yield {
                "title":title,
                "link":link,
                "tag":tag,
                "image":image
            }
