def rev_list_in_place(lst):
    """Reverse list in place.

    You cannot do this with reversed(), .reverse(), or list slice
    assignment!

    >>> lst = [1, 2, 3]

    >>> rev_list_in_place(lst)
    [3, 2, 1]

    >>> lst
    [3, 2, 1]

    """


    # initialize a variable called right index --> starting at 0
    # initialize a variable called left index --> starting at negative 1
    # current equal to zero
    # find the midpoint of list (length of the list divided by 2)
    # whole the current is less than the midpoint, (length of list divided by 2)
    # switch the index of the list-- list[right] == list[left]
    # increment right index by 1
    # decrement left index by 1
    # increment the pointer by 1


    # Walk through half of the list
    # for each item in the list, swap it with the item in the corresponding 
    # Position counting from the back
    # Issue is, we dont want to overwrite the value stored in either of those positions
    # So we can use a temp variable to store one of the values 
    # Or we can use the tuple unpacking syntax like x, y = y, x

    right_index = 0
    left_index = -1

    current = 0

    while current < (len(lst) / 2):
        lst[right_index], lst[left_index] = lst[left_index], lst[right_index]
        right_index += 1
        left_index -= 1
        current += 1

    return lst


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All tests passed yayy!"
