"""
This module contains the models:
- Article : For the TheGuardian articles
"""

import maya  # Package for data parsing

# Default value
NAN = 'Unknown'

class Article:
    """
    This class represents an article on TheGuardian and
    it contains :
    - url    : The link to the original article
    - author : The author of the article
    - tags   : The keywords representing the article
    - title  : The title of the article
    - date   : The published data
    - images : The images in html <img> format
    - body   : The whole text
    """

    def __init__(self, url=None, author=None, tags=None,
    title=None, date=None, images=None, body=None):
        """
        Natural constructor of the Article class.
        """
        has_elements = lambda x: True if len(x) > 0 else False

        self.url    = url[0]
        self.title  = title[0]
        self.date   = date[0]
        self.tags   = tags
        self.images = images
        self.body   = body
        self.author = author[0] if has_elements(author) else NAN

    def get_date(self):
        """
        This functions returns a string of a formatted date using
        the maya package.
        """
        # Parse the date
        date = maya.parse(self.date)

        # Get the datatime object from maya object
        dt = date.datetime()

        # Return in this format 'Thu Dec 10 17:48:28 2020'
        return dt.strftime('%c')

    def get_body(self):
        """
        This function return a string for the body text of the
        article instead of the list. 
        """
        # Create separator
        separator = "<br>"

        # Link the elements
        body = separator.join(self.body)

        return body
