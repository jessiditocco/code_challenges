def  lemur(branches):
    """Return number of jumps needed.
    >>> lemur([0])
    0

    >>> lemur([0, 0])
    1

    >>> lemur([0, 0, 0])
    1

    >>> lemur([0, 1, 0])
    1

    >>> lemur([0, 0, 1, 0])
    2

    >>> lemur([0, 0, 0, 0, 1, 0, 0, 1, 0])
    5
    """

    # O represents alive branches and 1 represent dead branches

    # keep track of the current index
    # keep track of the number of jumps: we will return this
    # use a while loop; while the current index is 1 below the length of the list
    # we want to set the index of current_index to +2
    # if the list at this position is 1 or we are out of range of the list, we want to decrement
    # our current_index to minus 1
    # increment our jumps by 1
   

    current_index = 0
    num_jumps = 0


    while current_index < len(branches) - 1:
        current_index += 2

        if current_index >= len(branches) or branches[current_index] == 1:
            current_index -= 1

        num_jumps += 1

    return num_jumps



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All tests passed"