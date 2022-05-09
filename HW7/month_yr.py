import pandas as pd
import calendar

from collections import Counter


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

def count_month_yr_1(x):

    """
    create new dara frame with month year count
    :param x: pd data frame
    :return: x pd data frame
    :rtype:
    """

    assert isinstance(x, pd.DataFrame)
    col = x['month-yr']
    count = Counter(col)
    newcount = pd.DataFrame(pd.Series(count))
    newcount.columns = ['Timestamp']

    return newcount

def count_month_yr(x):

    df = add_month_yr(x)
    month = df.groupby("month-yr").size()
    df = pd.DataFrame(month, columns=["Timestamp"])

    return df

def fix_categorical(x):

    """
    create new dara frame with month year count
    :param x: pd data frame
    :return: x pd data frame
    :rtype:
    """

    assert isinstance(x, pd.DataFrame)

    df = add_month_yr(x)
    categories = ["Sep-2017", "Jan-2018", "Feb-2018", "Mar-2018", "Apr-2018", "Sep-2018", "Oct-2018", "Jan-2019"]

    df["month-yr"] = pd.Categorical(df["month-yr"], ordered=True, categories = categories)
    df.groupby('month-yr')['Timestamp'].count().to_frame().sort_index()


    return df

def fix_categorical_1(x):

    """
    create new dara frame with month year count
    :param x: pd data frame
    :return: x pd data frame
    :rtype:
    """

    assert isinstance(x, pd.DataFrame)

    df = add_month_yr(x)
    categories = ["Sep-2017", "Jan-2018", "Feb-2018", "Mar-2018", "Apr-2018", "Sep-2018", "Oct-2018", "Jan-2019"]

    df["month-yr"] = pd.Categorical(df["month-yr"], ordered=True, categories = categories)
    df.groupby('month-yr')['Timestamp'].count().sort_values()

    return df


data = pd.read_csv("survey_data.csv")

#col = data['Is there anything in particular you want to use Python for?']
print(count_month_yr(add_month_yr(data)))


print(fix_categorical(data))



