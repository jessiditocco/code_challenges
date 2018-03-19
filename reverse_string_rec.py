# Given a string, return a new string that is the original string, reversed. Do this with recursion, not a for loop.

def rev_string(astring):
    """Return reverse of string using recursion.

    >>> rev_string("porcupine")
    'enipucrop'

    You may NOT use the reversed() function!
    """

    # base case is where there is only one letter; the first letter now equals the last letter

    if not astring:
        return astring

    n = 0

    return astring[-1] + rev_string(astring[:(n-1)])


print rev_string("porcupine")