# Given list of ints, return True if any two nums in list sum to 0.

def add_to_zero(nums):
    """ Checks to see if numbers in a list add to zero.   
        >>> add_to_zero([])
        False

        >>> add_to_zero([1])
        False

        >>> add_to_zero([1, 2, 3])
        False

        >>> add_to_zero([1, 2, 3, -2])
        True

        >>> add_to_zero([0, 1, 2])
        True
    """

    # making a set in python takes o(n) time
    nums = set(nums)
    # looping through numbers in the list takes o(n) time
    for num in nums:
        # searching for an item in a set takes constant time o(1)
        # python considers -0 == 0
        if (-num) in nums:
            return True
    
    return False

# This function will run in o(n) constant time


if __name__ == "__main__":
    import doctest
    doctest.testmod()
