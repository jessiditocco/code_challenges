def sort_ab(a, b):
    """Given already-sorted lists, `a` and `b`, return sorted list of both.

    You may not use sorted() or .sort().

    >>> a = [1, 3, 5, 7]
    >>> b = [2, 6, 8, 10]

    >>> sort_ab(a, b)
    [1, 2, 3, 5, 6, 7, 8, 10]

    """

    # we will intialize a list called sorted = []
    # reverse both a and b
    # while the length of list a or the length of list b is greater than 0
    # if the length of a is zero, extend sorted by b
    # if the length of b is zero, extend the sorted by a
    # if a at the last index is smaller than b at the last index, append a at last index
    # else, append b at the last index

    # This is merge sort implementation that take O(n)

######################### This is my Solution #########################
    # combined_sort = []
    # a.reverse()
    # b.reverse()


    # while len(a) > 0 or len(b) > 0:
    #     if len(a) == 0:
    #         combined_sort.append(b.pop())
    #     elif len(b) == 0:
    #         combined_sort.append(a.pop())
    #     elif a[-1] < b[-1]:
    #         combined_sort.append(a.pop())
    #     else:
    #         combined_sort.append(b.pop())

    # return combined_sort


######################### This is Hackbright Solution #########################
    
    # initialize a list called combined sort
    # initialize variables for index at a and index at b
    # check current items in both lists
    # if a < b, add it, and increase a ia by 1
    # if a > b, add b, and incresae ib by 1
    # extend the list by the a list from the current index to the end 
    # extend the list by the list b from the current index to the end


    combined_sort = []

    ia = 0 # index into list a
    ib = 0 # index into list b

    while ia < len(a) and ib < len(b):
        if a[ia] < b[ib]:
            combined_sort.append(a[ia])
            ia += 1
        else:
            combined_sort.append(b[ib])
            ib += 1

    combined_sort.extend(a[ia:])
    combined_sort.extend(b[ib:])

    return combined_sort




if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All tests passed"