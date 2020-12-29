"""
This module contains the models:
- Article    : For the TheGuardian articles
- Gas        : For the datasets related to CO2, NO2 and SO2
- Area       : For the datasets related to Terrestrial, Marine and Forest area
- Ressources : For the datasets related to Water and Renewable electricity sources
"""

import maya  # Package for data parsing
from textblob import TextBlob  # Package for text sentiment analysis
import pandas as pd  # Package for data analysis and manipulation 
import ssl

# Allow to read excel from the web
ssl._create_default_https_context = ssl._create_unverified_context

#-- Related to Article --#

# Default value for Article
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
        has_elements = lambda x: x[0] if len(x) > 0 else NAN

        self.url    = url if url else None
        self.title  = title[0] if title else None
        self.date   = date[0] if date else None
        self.tags   = tags if tags else None
        self.images = images if images else None
        self.body   = body if body else None
        self.author = has_elements(author) if author else NAN
        self.banner = has_elements(banner) if banner else NAN

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

        neg_score = int(-neg_score * 100)
        pos_score = int(pos_score * 100)
        total = pos_score + neg_score

        neg_score = 0 if total == 0 else (neg_score * 100) / total 
        pos_score = 0 if total == 0 else (pos_score * 100) / total 

        return round(neg_score) if negative else round(pos_score)

def is_link(string):
    if "www." in string:
        return True
    elif "http" in string:
        return True
    elif ".com" in string:
        return True
    else:
        return False

# Functions for list of Article
def articles_count(articles):
    """
    This function returns the length of the list.
    """
    return len(articles)

def average_letter_count(articles):
    """
    This function returns the average letter count of
    the articles.
    """
    letters = 0

    # Number of articles
    n = articles_count(articles)

    # Loop over the articles
    for article in articles:

        # Increment the letters count
        letters += len(article.get_body())

    return round(letters / n, 1)

def average_sentiment_score(articles):
    """
    This function returns a tuple of the average sentiment
    score for both positivity and negativity.
    """
    # articles count
    n = articles_count(articles)

    # Score
    negativity = 0
    positivity = 0

    # Loop over articles
    for article in articles:
        negativity += article.sentiment_score(negative=True)
        positivity += article.sentiment_score(negative=False)

    negativity = 0 if n == 0 else round(negativity / n, 1)
    positivity = 0 if n == 0 else round(positivity / n, 1)

    return (negativity, positivity)


#-- Related to Gas --#

# Links for excel files
GAS_LINKS = {
    "CO2":"https://unstats.un.org/unsd/environment/excel_file_tables/2013/CO2_Emissions.xlsx",
    "NO2":"https://unstats.un.org/unsd/environment/excel_file_tables/2013/NOx_Emissions.xlsx",
    "SO2":"https://unstats.un.org/unsd/environment/excel_file_tables/2013/SO2_emissions.xlsx"
}

# Units depending on the gas
GAS_UNITS = {
    "CO2": {"EMISSIONS": "M Tonnes", "PERCENTAGE":"%", "CAPITA":"Tonnes"},
    "NO2": {"EMISSIONS": "Thousand Tonnes", "PERCENTAGE":"%", "CAPITA":"Kg"},
    "SO2": {"EMISSIONS": "Thousand Tonnes", "PERCENTAGE":"%", "CAPITA":"Kg"}
}

class Gas:
    """
    This class will contain the data about the following
    gas emission :
    - 'CO2'
    - 'NO2'
    - 'SO2'
    """

    def __init__(self, gas_name):
        """
        Natural constructor of Gas.
        """
        self.name = gas_name
        self.link = GAS_LINKS.get(gas_name)
        try:
            # Get the data from the web
            data = pd.read_excel(self.link, header=17 if self.name == "SO2" else 16, engine='openpyxl')
            
            # Get the right columns and rows
            self.frame = data.iloc[1:, [1, 2, 4, 6, 8] if self.name == "CO2" else [1, 3, 5, 7]].dropna()

        except:
            print("Error in Gas instance creation. Reason : Link", flush=True)

#-- Related to Area --#

# Links for excel files
AREA_LINKS = {
    "FOREST"            :"https://unstats.un.org/unsd/envstats/Questionnaires/2019/Tables/Forest%20Area.xlsx",
    "TERRESTRIAL_MARINE":"https://unstats.un.org/unsd/envstats/Questionnaires/2019/Tables/Terrestrial_Marine%20protected%20areas.xlsx"
}

class Area:
    """
    This class will contain the data about the following
    protected area :
    - 'FOREST'
    - 'TERRESTRIAL_MARINE'
    """
    def __init__(self, area_name):
        """
        Natural constructor of Gas.
        """
        self.name = area_name
        self.link = AREA_LINKS.get(area_name)
        print(AREA_LINKS.get(area_name), flush=True)

        try:
            # Get the data from the web
            data = pd.read_excel(
                self.link, 
                engine='openpyxl', 
                sheet_name="data" if self.name == 'FOREST' else "Data", 
                index_col="CountryID"
            )

            # Get the data from the web
            self.frame = data.iloc[2:, :].dropna()

        except:
            print("Error in Area instance creation. Reason : Link", flush=True)

#-- Related to Ressources --#
