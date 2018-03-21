def is_leap_year(year):
    """Is this year a leap year?

    Every 4 years is a leap year::

        >>> is_leap_year(1904)
        True

    Except every hundred years::

        >>> is_leap_year(1900)
        False

    Except-except every 400::

        >>> is_leap_year(2000)
        True
    """

    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    if year % 4 == 0:
        return True


def days_in_month(date):
    """How many days are there in a month?

    >>> days_in_month("02 2015")
    28
    >>> days_in_month("01 2016")
    31
    >>> days_in_month("02 2016")
    29
    >>> days_in_month("03 2016")
    31
    >>> days_in_month("04 2016")
    30
    >>> days_in_month("05 2016")
    31
    >>> days_in_month("06 2016")
    30
    """

    month, year = date.split()
    month = int(month)
    year = int(year)

    # Account for february
    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28

    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    else:
        return 30


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\nALL TESTS PASSED!!! WOOOT\n"