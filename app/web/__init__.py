from flask import Flask
import os
from pymongo import MongoClient
from flask import render_template
from random import randint

app = Flask(__name__)  # Init the app

client = MongoClient('mongodb', 27017)

db = client['test']

collection = db['titles']

collection.insert_many([
    {"title":"The new president", "value":1},
    {"title":"The ancient president", "value":2},
    {"title":"The former president", "value":3},
    {"title":"The meter president", "value":4}
])

def add_data():
    collection.insert_one({"title":str(randint(1,200)), "value":int(randint(1,200))})

from web import views
