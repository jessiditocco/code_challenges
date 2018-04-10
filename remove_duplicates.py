def deduped(items):
    """Return new list from items with duplicates removed.
    
    >>> deduped([1, 1, 1])
    [1]

    >>> deduped([1, 2, 1, 1, 3])
    [1, 2, 3]

    >>> deduped([1, 2, 3])
    [1, 2, 3]

    >>> a = [1, 2, 3]

    >>> b = deduped(a)

    >>> a == b
    True

    >>> a is b
    False

    >>> deduped([])
    []

    """

    # # create an empty dictionary
    # # create an emtpy list that we will return 
    # # Loop through the items in the list, if the item is not in the dict, add item to the list, and to the dict
    # # If the item is in the dict, increase the count by 1
    # # If the item is in the dict already, dont add the item to the list
    # # return list


    # duplicate_counts = {}

    # deduped = []

    # for item in items:
    #     duplicate_counts[item] = duplicate_counts.get(item, 0) + 1


    #     if duplicate_counts[item] == 1:
    #         deduped.append(item)

    # return deduped

    ##################### HB SOLUTION ####################################

    # # sets are great for de-duplicating lists:
    # # sets dont maintain oder though, so if we want our answer to be in order
    # # we have to do the de-duplicating by hand
    # # however... this runtime would be O(n^2) becaause we have a for loop
    # # and nested inside that, we have an in which is a hidden for-loop
    # # for every charecter that we are looping over, we have to loop in deduped
    # # to check if that charecter is in there
    # # we dont want this 

    # deduped = []

    # for char in items:
    #     if char not in deduped:
    #         deduped.append(char)
    
    # return deduped

    # instead we can use use a set to keep track of what we have seen and use a list
    # to hold the final results

    # keep track of what we have seen
    seen = set()

    # deduped will be what we return 
    deduped = []

    for item in items:
        if item not in seen:
            deduped.append(item)
            seen.add(item)

    return deduped



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All tests passed!!"
