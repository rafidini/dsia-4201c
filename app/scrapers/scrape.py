import scrapy
from scrapy.crawler import CrawlerProcess
from theguardian.headlines import TGHeadlinesSpider
from config import FEED_URI, FEED_FORMAT

def scrape():
    scraped = {}
    process = CrawlerProcess({"FEED_URI":FEED_URI, 'FEED_FORMAT':FEED_FORMAT})
    process.crawl(TGHeadlinesSpider, outputResponse=scraped)
    process.start(stop_after_crawl=True)
    return scraped

if __name__=='__main__':
    scrape()
