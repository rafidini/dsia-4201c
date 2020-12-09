import scrapy

class TGArticleSpider(scrapy.Spider):
    name = 'tg-article'
    allowed_domains = ['theguardian.com']

    def __init__(self, *args, **kwargs):
        super(TGArticleSpider, self).__init__(*args, **kwargs)
        url = getattr(self, 'url', False)

        if len(kwargs) <= 1 and not url:
            self.start_urls = ['https://www.theguardian.com/environment']

        else:
            # Runned with : scrapy runspider article.py -a url=https://www.theguardian.com/environment/2020/dec/09/what-would-a-climate-friendly-uk-mean-for-you
            self.start_urls = [url]

    def parse(self, response):
        author = response.xpath('//meta[@property="article:author"]/@content').extract()
        title  = response.xpath('//meta[@property="og:titlehor"]/@content').extract()
        tags   = response.xpath('//meta[@property="article:tag"]/@content').extract()
        date   = response.xpath('//meta[@property="article:published_time"]/@content').extract()
        images = response.xpath("//div[@itemprop='articleBody']").css('img').extract()
        body   = response.xpath("//div[@itemprop='articleBody']").css('p').extract()

        yield {
            'url': self.start_urls[0],
            'tags': tags,
            'date': date,
            'images': images,
            'body': body
        }
