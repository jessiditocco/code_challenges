def split(astring, splitter):
    """Split a string by splitter and return list of splits.

    >>> split("i love balloonicorn", " ")
    ['i', 'love', 'balloonicorn']

    >>> split("that is which is that which is that", " that ")
    ['that is which is', 'which is that']

    >>> split("that is which is that which is that", "that")
    ['', ' is which is ', ' which is ', '']

    >>> split("hello world", "nope")
    ['hello world']

    """

    # loop through the string using enumerate so we can keep track 
    # keep track of start_of_word
    # make an empty list 
    # of value and index
    # if value equal splitter, split the string from start of word
    # and append it to the list
    # to the index that you are one
    # set start of word to the index you are on plus 1


    # splits = []
    # start = 0

    # for i, char in enumerate(astring):
    #     if char == splitter:
    #         splits.append(astring[start:i])

    #         start = i + 1

    # return splits







    # keep track of start
    # intialize an empty list
    # loop through the indices and letters using enumerate
    # if the charecter that you are on is equal to the spliter
    # slice from start to that index and append it to the list
    # update start to that new indice + 1

    start = 0

    split = []

    for i, char in enumerate(astring):
        print i, char
        if char == splitter:
            print astring[start:i]
            split.append(astring[start:i])
            start = i + 1

    return split

split("i love balloonicorn", " ")






if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All tests passed!!"


