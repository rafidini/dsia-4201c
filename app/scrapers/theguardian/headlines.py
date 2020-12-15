import datetime
import scrapy
from date.date import date_to_theguardian  # local package for date operations

TODAY = datetime.datetime.now()

class TGHeadlinesSpider(scrapy.Spider):
    name = 'tg-headlines'
    allowed_domains = ['theguardian.com']

    def __init__(self, *args, **kwargs):
        super(TGHeadlinesSpider, self).__init__(*args, **kwargs)
        date = getattr(self, 'date', False)  # For a single date
        dates = getattr(self, 'dates', False)  # For multiple dates

        if len(kwargs) <= 1 and not date:  # When there are no args
            self.start_urls = ['https://www.theguardian.com/environment']

        else:
            if date:
                # Runned with : scrapy runspider headlines.py -a date=2020-03-27
                # Runned with : scrapy runspider headlines.py -a date=YYYY-MM-DD
                date = datetime.datetime.strptime(date, "%Y-%m-%d")

            elif dates:
                # Runned like : scrapy runspider headlines.py  -a dates=[dt1, dt2]
                links = [date_to_theguardian(d) for d in dates]
                self.start_urls = links

            else:
                # Runned with : scrapy runspider headlines.py -a year=2020 -a month=2 -a day=2
                # Runned with : scrapy runspider headlines.py -a year=2020 -a month=2 -a day=16
                date = datetime.datetime(
                    int(getattr(self, 'year', TODAY.year)),
                    int(getattr(self, 'month', TODAY.month)),
                    int(getattr(self, 'day', TODAY.day))
                )

            if not dates:
                self.start_urls = [f'https://www.theguardian.com/environment/{date.strftime("%Y")}/{date.strftime("%b").lower()}/{date.strftime("%d")}/all']

    def parse(self, response):
        articles = response.css(".fc-item__container")  # Extract the articles
        items = []
        for article in articles:  # Loop over the articles
            title = article.xpath('a/text()').extract()
            link = article.xpath('a/@href').extract()
            tag = article.xpath('.//span[@class="fc-item__kicker"]/text()').extract()
            image = article.xpath('.//source/@srcset').extract_first()

            item = {
                "title":title,
                "link":link,
                "tag":tag,
                "image":image
            }

            items.append(item)

            yield item
        
        self.outputResponse['items'] = items
