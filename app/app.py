from web import app  # local package for the initiated Flask App
from scrapers.scrape import scrape  # local package for the web scraping
from datetime import datetime

if __name__=='__main__':

    last_update = datetime(2020, 10, 1)  # Example of a last update from MongoDB

    head, arti = scrape(last_update)  # Extract data from today's headlines
    
    print(f"[0] Extracted : {head}")
    print(f"[1] Extracted : {arti}")

    app.run(host='0.0.0.0', port=5000)  # Run the Flask App
