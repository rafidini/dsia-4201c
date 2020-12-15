"""
This module will contains the functions that process datetime for the
webscraping.
"""

from datetime import datetime, timedelta

# TheGuardian link in string format
# [0] year  : integer (ex: 2001, 1920, 2010)
# [1] month : string  (ex: jan, dec, jun)
# [2] day   : integer (ex: 1, 10, 30)
THEGUARDIAN_BASE = "https://www.theguardian.com/environment/{}/{}/{}/all"

def get_dates_since(last_date, first_date=datetime.today()):
    """
    This function returns a list of datetime object from
    the given date until today. 
    """

    dates = []  # Will contain the dates

    today = first_date  # Get today's date

    difference = int( ( today - last_date ).days + 1)  # Get the difference of days

    for i in range(difference): # Iterate over the number of days
        dates.append( last_date + timedelta(i) )  # Append dates

    return dates

def date_to_theguardian(date):
    """
    This function return the link of a TheGuardian page listing
    the articles in environement section.

    >>> date_to_theguardian(datetime(2020, 4, 19))
    https://www.theguardian.com/environment/2020/apr/19/all
    """

    year = date.year  # Extract the year

    month = date.strftime("%b").lower()  # Extract the month

    day = date.day  # Extract the day

    return THEGUARDIAN_BASE.format(year, month, day)

