from web import app  # local package for the initiated Flask App
from datetime import datetime
import json

if __name__=='__main__':

    with open('articles.json') as f:
        articles = json.load(f)

    print("ARTICLES :", len(articles['items']))

    del articles

    app.run(host='0.0.0.0', port=5000)  # Run the Flask App
