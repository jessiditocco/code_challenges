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


    # .find("sub") method in python take a substring
    # .find("sub", start, end) -- takes a start and end argument-- start is incluive
    # end is not inclusive
    # If the substring exitst inside of the string, it returns the lowest index
    # where the substring is found
    # if the substring doesn't exist, it returns -1

    # initialize an empty list called split
    # keep track of the start index --> starting at 0
    # while start index is less than the length of the list:
    # use find, searching like astring.find("splitter", start)
        # this will return the lowest index of the found value
        # splice the list from start to this index and add it to the list
        # update start to split on plus 1
    # return the split list

    # out = []
    # index = 0

    # while index <= len(astring):
    #     curr_index = index
    #     index = astring.find(splitter, index)

    #     if index != -1:
    #         out.append(astring[curr_index:index])
    #         index += len(splitter)
    #     else:
    #         # couldn't find any more instances of splitter in astring
    #         out.append(astring[curr_index:])
    #         break 

    # return out



    # we need to keep track of our split list
    # we need to keep track of the index that we are on

    # while index is less than the length of the list
    # we want to keep track of the current index
    # we also want to reset index to the astring.find(splitter, index)
    # then, we want to check that the index returned is not -1 (which would mean there are no instances of the splitter)
    # if the index returned is not negative 1, we want to slice and append from curr index
    # to the index of the splitter
    # then we will increment the index by the length of the splitter
    # if the index of find comes out to -1, this means that there are no more 
    # instances of splitter so we will append the string from the current index to the end of the string



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All tests passed!!"


