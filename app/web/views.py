from flask import Flask, redirect, render_template, request, url_for
from . import app, collection
from db.utils import random_item, from_item_to_article, search_similar_articles, search_n_last_articles
from web.models import Article

@app.route('/')
@app.route('/home')
def home():
    # Number of articles
    n = 15

    # Extract articles
    articles = search_n_last_articles(n, collection)

    return render_template('index.html', articles=articles)

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/facts')
def facts():
    return render_template('facts.html')

@app.route('/article/<title>')
def article(title):
    # Query the database for the corresponding article
    items = collection.find({"title":title})

    # Converto to an Article instance
    article = from_item_to_article(items[0])

    # Look for similar articles
    similars = random_item(3, collection)

    return render_template('article.html', article=article, similar_articles=similars)

@app.route('/random')
def random():
    # Query the database for a random article
    size = 1
    items = random_item(1, collection)
    item = items[0]

    # Convert to an Article instance
    article = from_item_to_article(item)

    # Look for similar articles
    similars = random_item(3, collection)

    return render_template('article.html', article=article, similar_articles=similars)
