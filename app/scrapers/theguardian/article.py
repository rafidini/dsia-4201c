import scrapy
import json
from subprocess import check_output

class TGArticleSpider(scrapy.Spider):
    name = 'tg-article'
    allowed_domains = ['theguardian.com']
    output = list()

    def __init__(self, *args, **kwargs):
        super(TGArticleSpider, self).__init__(*args, **kwargs)
        has_json = getattr(self, 'json', False)
        links = getattr(self, 'links', False)
        filepath = getattr(self, 'filepath', None)

        if has_json:  # Extract 'start_urls' from json file
            json_urls = None

            with open(filepath) as f:  # Load the json file
                v_json = json.load(f)

            check_output(['rm', '-f', filepath])  # Delete the file

            self.start_urls = [ headline['link'] for headline in v_json ]

        elif links:
            self.start_urls = links

    def bodyExtracted(self, body):
        #  Expected extracting with 'articleBody' in itemprop
        if isinstance(body, list):
            #  The case the data was extracted
            if len(body) >= 1:
                return True
        return False

    def parse(self, response):
        title  = response.xpath('//meta[@property="og:title"]/@content').extract()
        tags   = response.xpath('//meta[@property="article:tag"]/@content').extract()
        date   = response.xpath('//meta[@property="article:published_time"]/@content').extract()
        images = response.xpath("//div[@itemprop='articleBody']").css('img').xpath('@src').extract()
        body   = response.xpath("//div[@itemprop='articleBody']").css('p').xpath('string()').extract()
        author = response.xpath('//meta[@property="article:author"]/@content').extract()
        banner = response.xpath('//body').css('img').xpath('@src').extract()

        if not self.bodyExtracted(body):
            body = response.css('p').xpath('string()').extract()

        item = {
            'url': self.start_urls[0],
            'author': author,
            'tags': tags,
            'title': title,
            'date': date,
            'images': images,
            'body': body,
            'banner': banner
        }

        yield item

        self.output.append(item)

        self.outputResponse['items'] = self.output

