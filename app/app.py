from web import app  # Import for the initiated Flask App
import subprocess
from scrapers.scrape import scrape


if __name__=='__main__':

    app.run(host='0.0.0.0', port=5000)  # Run the Flask App
