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


    nums = set(nums)

    for num in nums:
        if (-num) in nums:
            return True
    
    return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
