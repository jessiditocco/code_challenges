def print_digits(num):
    """Given int, print digits in reverse order, starting with the ones place

    >>> print_digits(1)
    1

    >>> print_digits(314)
    4
    1
    3

    >>> print_digits(12)
    2
    1

    """

    # Given an integer, print each digit in reverse order, starting with the ones place.

    # # For example, if you were given 1 you should simply print 1, if given 314 you should print 4, 1, 3, and if given 12 you should print 2, 1:

    # Implement print_digits. Do not do this by just turning the number into a string and reversing it. Solve the problem using math.
    
    while num:
        next_digit = num % 10
        print next_digit

        num = (num - next_digit) / 10

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "Passed all tests!!!!"