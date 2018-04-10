def print_recursively(lst):
    """Print items in the list, using recursion.

    >>> print_recursively([1, 2, 3])
    1
    2
    3

    """

    # if not lst:
    #     return 

    # print lst[0]

    # print_recursively(lst[1:])

    if lst:
        print lst[0]
        print_recursively(lst[1:])

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All tests passed!"