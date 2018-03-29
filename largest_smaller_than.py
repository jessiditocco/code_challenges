def find_largest_smaller_than(nums, xnumber):
    """Find largest number in sorted list that is smaller than given number.

    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 10)
    2

    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 33)
    4

    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], -1)
    1

    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 8)
    2

    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], -10) is None
    True

    """

# Given an ordered list of numbers and a number, 
# return the index of the largest number in the list that is 
# smaller than that number.

    # loop through each number in the list
    # check to see if the number is smaller than the xnumber, update largest number variable
    # return largest_number

    largest_index = None

    for i in range(len(nums)):
        if nums[i] <= xnumber:
            largest_index = i
            

    return largest_index


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "yay passed all tests"