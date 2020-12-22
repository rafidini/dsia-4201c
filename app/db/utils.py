"""
This module contains the functions that operation the
database.
"""

from pymongo import MongoClient
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

