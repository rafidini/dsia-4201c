"""
This module loads articles, body and stuff.
"""

from scrapers.scrape import scrape_articles
from datetime import datetime
import json
from subprocess import check_output

if __name__=='__main__':
    # Get links 
    with open('links.json') as f:
        links = json.load(f)

    # Scrape
    articles = scrape_articles(links)

    # Delete file
    check_output(['rm', '-f', 'links.json'])

    # Save articles
    with open('articles.json', 'w') as f:
        json.dump(articles, f)
