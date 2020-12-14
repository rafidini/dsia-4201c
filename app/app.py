from web import app  # Import for the initiated Flask App
import subprocess
from scrapers.scrape import scrape


if __name__=='__main__':

    # This part exctract data from today's headlines
    data = scrape()
    print("----------------------------")
    print(f"Extracted : {data}")

    app.run(host='0.0.0.0', port=5000)  # Run the Flask App
