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

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.route('/news')
@app.route('/news/<tag>')
def news(tag=None):

    if tag:
        print(f'Tag is {tag}', flush=True)
        tag = tag.replace("%20", " ")

    # Query the database if tag is given
    query = {'tags':tag} if tag else {}

    # Launch the query
    items = collection.find(query)
    articles = list()

    for item in items: 
        print("ITEMS TAGS :", item['tags'], flush=True)
        articles.append(from_item_to_article(item))    

    # Get tags
    try:
        del v_tags
    except:
        pass

    v_tags = set()
    for article in articles:
        for a_tag in article.tags:
            v_tags.add(a_tag)

    return render_template('news.html', tag=tag, articles=articles, tags=v_tags)

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
    similars = [from_item_to_article(item) for item in collection.find().limit(3)]

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
