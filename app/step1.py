"""
This module loads the headlines and links of articles.
"""

from scrapers.scrape import scrape_links
from datetime import datetime
import json
from subprocess import check_output

if __name__=='__main__':
    # Begin date
    date = datetime(2020, 12, 29)
    
    # Get links
    scrape_links(date)

    # Open headlines
    with open('data/headlines.json') as f:
        items = json.load(f)

    check_output(['rm', '-f', 'data/headlines.json'])

    links = [item['link'][0] for item in items]
    
    # Save links
    with open('links.json', 'w') as f:
        json.dump(links, f)
