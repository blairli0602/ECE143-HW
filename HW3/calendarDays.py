import calendar

def number_of_days(year,month):
    """
    function that returns the number of calendar days in a given year and month.
    param year: int, month: int
    return: int number of calendars days
    """

    assert isinstance(year, int)
    assert isinstance(month, int)
    assert year > 0 and 0 < month <= 12

    x = calendar.Calendar()
    result = []
    result = calendar.monthrange(year,month)[1]
    return result


def number_of_leap_years(year1,year2):
    """
    find the number of leap-years between (including both endpoints) two given years
    param: year1: begin year2: end
    return: int numer of leap years
    """
    assert isinstance(year1, int)
    assert isinstance(year2, int)
    assert 0 < year1 <= year2 and 0 < year2

    result = 0
    result = calendar.leapdays(year1, year2+1)

    return result


def get_day_of_week(year,month,day):
    """
    string name (e.g., Monday, Tuesday) of the day of the week on a given month,day, and year
    param year, month day: int
    return: Mon - Sun
    """

    assert isinstance(year, int)
    assert isinstance(month, int)
    assert isinstance(day,int)

    if month == 2 and day == 29:
        assert calendar.isleap(month) is True

    assert year > 0 and month > 0 and day > 0

    day = calendar.weekday(year,month,day)

    dayName = calendar.weekheader(10)
    dayName = list(dayName.split())

    day = dayName[day]

    return day
