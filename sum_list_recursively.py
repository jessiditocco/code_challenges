def sum_list(nums):
    """Using recursion, return the sum of numbers in a list.

    For example::

    >>> sum_list([5, 5])
    10

    >>> sum_list([-5, 10, 4])
    9

    >>> sum_list([20])
    20

    The sum of an empty list is zero::

    >>> sum_list([])
    0
    """

    # basecase will be when the length of the list is equal to zero

    # return the list[0] + sum_list[1:]

    # remember, when we are summing a list recursively, in the basecase, 
    # we must return 0 when we get to an empty list because if we just
    # return None, we cannot add None type and integer
    
    if not nums:
        return 0 

    return nums[0] + sum_list(nums[1:])


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All tests passed!"