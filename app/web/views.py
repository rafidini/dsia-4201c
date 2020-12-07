from flask import Flask, redirect, render_template, request, url_for
from . import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/news')
def category():
    return render_template('news.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/facts')
def facts():
    return render_template('facts.html')

@app.route('/article')
def article():
    return render_template('article.html')
