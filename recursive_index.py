def recursive_search(needle, haystack, current_index=0):
    """Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.
    >>> lst = ["hey", "there", "you"]

    >>> recursive_search("hey", lst)
    0

    >>> recursive_search("you", lst)
    2

    >>> recursive_search("porcupine", lst) is None
    True

    """

    # Our basecase for a recursive search would be if our current index
    # Was out of the range of the length of the list
    # We want to return none of we get to the end and dont find the needle
    # We will check if the needle is equal to the haystack at the current index
    # If so, return the current index
    # If not, call recursive search, passing needle, haystack, and the current index
    # incremented by 1

    if current_index > (len(haystack) - 1):
        return None

    if needle == haystack[current_index]:
        return current_index

    return recursive_search(needle, haystack, current_index + 1)





if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All tests passed yay!"
