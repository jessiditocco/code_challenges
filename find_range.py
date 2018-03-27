def find_range(nums):
    """Given list of numbers, return smallest & largest number as a tuple.
    >>> find_range([3, 4, 2, 5, 10])
    (2, 10)

    >>> find_range([43, 3, 44, 20, 2, 1, 100])
    (1, 100)

    >>> find_range([])
    (None, None)

    >>> find_range([7])
    (7, 7)
    """

    # sort the list
    # make a tuple with the list at index 0 and index -1
    # if empty list, make tuple of none and none

    # if not nums:
    #     return (None, None)

    # nums.sort()

    # return (nums[0], nums[-1])

    # without using sort()
    # if the list is empty, return tuple (None,None)
    # initialize a variable called smallest, and largest -- the first number in the list
    # loop through, if number is smaller than smallest, update
    # if the number is larger than the largest, update
    # return tuple with smallest and largest

    if not nums:
        return (None, None)

    smallest = nums[0]
    largest = nums[0]

    for num in nums:
        if num < smallest:
            smallest = num

        elif num > largest:
            largest = num

    return (smallest, largest)



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "ALL TESTS PASSEd!!!"
