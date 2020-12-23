"""
This module contains the functions that operation the
database.
"""

from pymongo import MongoClient
from web.models import Article
import json

# Constants for MongoDB
MONGODB = 'mongodb'
PORT    = 27017

def init_db(db_name, collection_name=None):
    """
    This function initiate a MongoDB, by returning the given
    collection name from the given database name.
    """

    # Initiate the MongoClient
    client = MongoClient(MONGODB, PORT)

    # Get the database named with the db_name value
    database = client[db_name]

    # If given, get the corresponding collection
    if collection_name:
        collection = database[collection_name]

        return database, collection

    # Just return the database otherwise
    return database

def feed_db_json(filepath, collection):
    """
    This function feed the collection in a database with the
    items in the file given by its path.
    """
    i = 0

    # Open the json file
    with open(filepath) as f:
        # Load the json file as a python dictionary
        items = json.load(f)

    # Loop over the items
    for item in items['items']:
        try:
            # Insert the item in the collection
            collection.insert_one(item)
            i += 1
        except:
            pass

    print(f'> {i} items were saved in the database.')
    print(f"> {len(items['items']) - i} items were not saved in the database.")

def random_item(size, collection):
    """
    This function returns random items from a given collection, 
    the number of items is given by the parameter size.
    """

    # Extract the random item(s)
    items = collection.aggregate([{'$sample': {'size':size}}])

    # Convert them into a list
    return [element for element in items]

def from_item_to_article(item):
    """
    This function initialize an Article instance from
    an extracted item from the MongoDB collection.
    """
    article = Article(
        url=item['url'],
        author=item['author'],
        tags=item['tags'],
        title=item['title'],
        date=item['date'],
        images=item['images'],
        body=item['body'],
        banner=item['banner']
    )

    return article

def search_similar_articles(article, collection, max_articles=3):
    """
    This function queries the collection to look for similar
    articles to the given one, and return them as a list of
    Article instances.
    """

    # Define the query
    # query = {}

    # Launch the query
    # items = collection.find(query).limit(max_articles)

    # TODO - Comment this
    items = random_item(max_articles, collection)

    # Convert items to list of Article
    articles = [from_item_to_article(item) for item in items]

    return articles

def search_n_last_articles(n, collection):
    """
    This functions returns n articles.
    """
    return [from_item_to_article(item) for item in collection.find({}).limit(n)]
