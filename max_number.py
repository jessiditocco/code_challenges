def max_num(num_list):
    """Returns largest integer from given list
    
    >>> max_num([5, 3, 6, 2, 1])
    6

    """

    max_num = num_list[0]

    for num in num_list:
        if num > max_num:
            max_num = num

    return max_num


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All tests passed!"