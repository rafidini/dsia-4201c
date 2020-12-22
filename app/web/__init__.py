from flask import Flask
import os
from pymongo import MongoClient
from flask import render_template
from db.utils import init_db, feed_db_json
from subprocess import check_output

# Init the app
app = Flask(__name__)

# Init MongoDB
database, collection = init_db('test', collection_name='articles')

# Feed MongoDB from the webscraping
filename = 'articles.json'
feed_db_json(filename, collection=collection)
check_output(['rm', '-f', filename])

# The views/pages
from web import views
