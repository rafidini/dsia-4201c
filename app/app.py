from web import app  # Import for the initiated Flask App
from subprocess import check_output



if __name__=='__main__':

    check_output(['python3', 'app/scrapers/scrape.py'])  # Run the scraping of headlines

    app.run(host='0.0.0.0', port=5000)  # Run the Flask App
