from web import app
from scrapers.scrape import scrape

#headlines = scrape()

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)
