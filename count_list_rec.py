# Count the items in a list recursively

def count_recursively(lst):
    """Return number of items in a list, using recursion.
    >>> count_recursively([])
    0

    >>> count_recursively([1, 2, 3])
    3
    """

    # If the list is empty, break out-- this is our basecase-- return 0

    if not lst:
        return 0

    # We want to slice the list in order to remove one item from the list
    # Each time we call count recursivley
    n = len(lst)
    return 1 + count_recursively(lst[:n-1])



if __name__ == "__main__":
    import doctest
    doctest.testmod()