import scrapy
from scrapy.crawler import CrawlerProcess
from scrapers.theguardian import headlines

FEED_URI = 'data/headlines.json'  # Path to the saved file 

def scrape():
    scraped = {}
    process = CrawlerProcess({"FEED_URI":FEED_URI})
    process.crawl(headlines.TGHeadlinesSpider, outputResponse=scraped)
    process.start(stop_after_crawl=True)
    return scraped

if __name__=='__main__':
    scrape()
