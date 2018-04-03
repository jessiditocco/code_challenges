def missing_number(lst_nums, max_num):
    """
    >>> missing_number([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)
    8
    """

    numbers = set(lst_nums)

    for i in range(1, max_num + 1):
        if i not in numbers:
            return i



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All tests passed!!"


