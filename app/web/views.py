from flask import Flask, redirect, render_template, request, url_for
from . import app, collection
from db.utils import random_item, from_item_to_article, search_similar_articles, search_n_last_articles
from web.models import Article, articles_count, average_letter_count, average_sentiment_score, Ressources

Ressources('ELECTRICITY')
Ressources('WATER')

@app.route('/')
@app.route('/home')
def home():
    # Number of articles
    n = 15

    # Extract articles
    articles = search_n_last_articles(n, collection)

    return render_template('index.html', articles=articles)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.route('/news')
@app.route('/news/<tag>')
def news(tag=None):

    # Cleaning the string
    if tag:
        tag = tag.replace("%20", " ")

    # Query the database if tag is given
    query = {'tags':tag} if tag else {}

    # Launch the query
    items = collection.find(query)
    articles = list()

    for item in items: 
        articles.append(from_item_to_article(item))    

    # Clean tags
    try:
        del v_tags
    except:
        pass

    # Every tags
    v_tags = set()
    for article in articles:
        for a_tag in article.tags:
            v_tags.add(a_tag)

    # Get the statistics
    stats = [
        articles_count(articles),
        average_letter_count(articles),
        average_sentiment_score(articles)
    ]

    return render_template('news.html', tag=tag, articles=articles, tags=v_tags, stats=stats)

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
    similars = [item for item in search_similar_articles(article, collection, max_articles=4)]

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
