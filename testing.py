def adder(x, y):
    """Adds two numbers
    >>> adder(1, 1)
    2

    >>> adder(0, 8)
    8

    """

    return x + y

assert adder(1, 1) == 2, '1 + 1 is not 2'


def print_range(number):
    """Prints the range using Ellipsis option
    >>> range(16) # doctest: +ELLIPSIS
    [0, 1, ..., 14, 15]

    """

    return range(number)



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All doctests passed!"
        # Tests pass, so we can start our server
        # app.run(debug=True)