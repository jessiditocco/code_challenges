def sum_list(num_list):
    """Return the sum of all numbers in list.

    >>> sum_list([5, 3, 6, 2, 1])
    17
    """

    # initialize a sum variable
    # loop through the list and increment sum by the number we are on
    # return sum

    sum_nums = 0

    for num in num_list:
        sum_nums += num

    return sum_nums


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All tests passed"