def rev_string(astring):
    """Return reverse of string using recursion.

    You may NOT use the reversed() function!

    >>> rev_string("porcupine")
    'enipucrop'
    """

    # basecase: if the length of the string is 1 letter, return the string
    # return string[-1] + reverse_string with arguments
    # a string sliced from : to -1

    if len(astring) < 2:
        return astring

    return astring[-1] + rev_string(astring[: -1])


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All tests passed!"