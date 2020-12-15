import scrapy
from scrapy.crawler import CrawlerProcess
from scrapers.theguardian.headlines import TGHeadlinesSpider
from scrapers.theguardian.article import TGArticleSpider
from scrapers.config import FEED_URI, FEED_FORMAT, DOWNLOAD_DELAY
from date.date import get_dates_since  # local package for date operations
from datetime import datetime

def scrape_links(date=datetime.today()):
    scraped_headlines = {}  # Will get the scraped data

    dates = get_dates_since(date)  # Get dates since the given date until today

    # CrawlerProcess
    process = CrawlerProcess({'DOWNLOAD_DELAY':DOWNLOAD_DELAY, 'FEED_URI':FEED_URI, 'FEED_FORMAT':FEED_FORMAT})  # Init the crawl
    process.crawl(TGHeadlinesSpider, dates=dates, outputResponse=scraped_headlines)
    process.start(stop_after_crawl=True)
    
    return scraped_headlines['items']

def scrape_articles(links):
    scraped_articles = {}  # Will get the scraped data

    # CrawlerProcess
    process = CrawlerProcess({'DOWNLOAD_DELAY':DOWNLOAD_DELAY})  # Init the crawl
    process.crawl(TGArticleSpider, links=links, outputResponse=scraped_articles)
    process.start(stop_after_crawl=True)
    
    return scraped_articles
