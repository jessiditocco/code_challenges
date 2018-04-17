def rev_string(astring):
    """Return reverse of string.

    You may NOT use the reversed() function!

    >>> rev_string("porcupine")
    'enipucrop'

    """

    # make an empty list
    # loop through letters from range of length of the string to the end 
    # backstepping by 1
    # append the letter to the list
    # join the list and return the string

    reversed_string = ""

    for i in range(len(astring), 0, -1):
        reversed_string += astring[i - 1]

    return reversed_string


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "Passed all tests!"