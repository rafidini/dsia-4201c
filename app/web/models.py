"""
This module contains the models:
- Article : For the TheGuardian articles
"""

import maya  # Package for data parsing
from textblob import TextBlob  # Package for text sentiment analysis

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
    - images : The images links
    - body   : The whole text
    - banner : The main image, displayed first
    """

    def __init__(self, url=None, author=None, tags=None,
    title=None, date=None, images=None, body=None, banner=None):
        """
        Natural constructor of the Article class.
        """
        has_elements = lambda x: True if len(x) > 0 else False

        self.url    = url
        self.title  = title[0]
        self.date   = date[0]
        self.tags   = tags[0].lower().split(',') if has_elements(tags) else [NAN]
        self.images = images
        self.body   = body
        self.author = author[0] if has_elements(author) else NAN
        self.banner = banner[0] if has_elements(banner) else NAN

    def get_date(self, short=False):
        """
        This functions returns a string of a formatted date using
        the maya package.
        """
        # Parse the date
        date = maya.parse(self.date)

        # Get the datatime object from maya object
        dt = date.datetime()

        # Return in this format 'Thu, 10 Dec 2020' or 'Dec, 10 2020'
        format_date = '%b, %d %Y' if short else '%a, %d %b %Y'

        return dt.strftime(format_date)

    def get_author(self):
        """
        This function returns the author.
        """

        # Check if given author is a link
        if is_link(self.author):
            # Split the string
            splitted = self.author.split('/')

            # Get the author
            author = splitted[-1]

            # Some cleaning
            author = author.replace('-', ' ')

            return author

        return self.author

    def has_author_link(self):
        """
        This function returns True if the author given is a link
        otherwise False.
        """
        # Check if given author is a link
        if is_link(self.author):
            return True
        else:
            return False

    def has_banner(self):
        """
        This functions returns True if the Article instance
        contains or not a banner image.
        """
        if self.banner != NAN:
            return True

        return False

    def has_images(self):
        """
        This function return True if there are images
        otherwise False.
        """
        if len(self.images) > 0:
            return True
        return False

    def get_body(self):
        """
        This function returns the whole body of the article as
        a single string.
        """

        # Join every elements in body
        whole = ' '.join(self.body)

        return whole

    def is_negative(self):
        """
        This function return True if the text is more negative otherwise
        False.
        """
        blob = TextBlob(self.get_body())  # Instanciate a TextBlob

        sentiment_score = blob.sentiment.polarity  # Score of the sentiment

        return sentiment_score < 0.0

    def sentiment_score(self, negative=False):
        """
        This function returns the absolute score in percentage.
        """

        # Counters
        neg = 0
        pos = 0

        # Scores
        neg_score = 0
        pos_score = 0

        # Loop over sentences
        for sentence in self.body:
            blob = TextBlob(sentence)  # TextBlob init

            score = blob.sentiment.polarity  # Compute sentiment score

            if score < 0:
                neg_score += score
                neg += 1

            elif score > 0:
                pos_score += score
                pos += 1 

        neg_score = 0 if neg == 0 else neg_score / neg
        pos_score = 0 if pos == 0 else pos_score / pos

        return int(-neg_score * 100) if negative else int(pos_score * 100)
        



def is_link(string):
    if "www." in string:
        return True
    elif "http" in string:
        return True
    elif ".com" in string:
        return True
    else:
        return False
