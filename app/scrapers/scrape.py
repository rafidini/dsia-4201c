import scrapy
from scrapy.crawler import CrawlerProcess
from scrapers.theguardian.headlines import TGHeadlinesSpider
from scrapers.theguardian.article import TGArticleSpider
from scrapers.config import FEED_URI, FEED_FORMAT

def scrape():
    scraped = {}
    process = CrawlerProcess({"FEED_URI":FEED_URI, 'FEED_FORMAT':FEED_FORMAT})
    process.crawl(TGHeadlinesSpider, outputResponse=scraped)
    process.crawl(TGArticleSpider, json=True, filepath=FEED_URI, outputResponse=scraped)
    process.start(stop_after_crawl=True)

    print("Scraped :", scraped)

    return scraped

if __name__=='__main__':
    scrape()
