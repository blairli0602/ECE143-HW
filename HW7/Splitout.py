import pandas as pd
from collections import Counter

from datetime import datetime
import calendar

def split_count(x):
    """
   split_count that can take this column as input and output the following Pandas dataframe.
    :param X:
    :type X: series
    :return: pd dataframe
    """
    assert isinstance(x, pd.Series)

    fullitems = []

    for items in x:
        fullitems.extend((items.split(', ')))

    count = Counter(fullitems)
    newcount = pd.DataFrame(pd.Series(count))
    newcount.columns = ['count']
    newcount = newcount.sort_values(by='count')

    return newcount


def add_month_yr(x):

    """
    add bew column month-yr
    :param x: pd data frame
    :return: x pd data frame
    :rtype:
    """

    assert isinstance(x, pd.DataFrame)

    x['year'] = pd.DatetimeIndex(x['Timestamp']).year
    x['month'] = pd.DatetimeIndex(x['Timestamp']).month

    month = []
    for i in x['month']:
        month.append(calendar.month_abbr[i])

    x['monthNew'] = pd.Series(month)
    x['month-yr'] = x['monthNew'].map(str) + '-' + x['year'].map(str)

    return x

data = pd.read_csv("survey_data.csv")

col = data['Is there anything in particular you want to use Python for?']
#print(split_count(col))


print(add_month_yr(data))