def show_evens(nums):
    """Given list of ints, return list of *indices* of even numbers in list.'
    >>> lst = [1, 2, 3, 4, 6, 8]

    >>> show_evens(lst)
    [1, 3, 4, 5]

    """

    # using list comprehension:
    # if num % 2 is equal to zero, return the indices as list

    return [i for i, num in enumerate(nums) if num % 2 == 0]

    # without list comprehension:

    evens = []

    for i, num in enumerate(nums):
        if num % 2 == 0:
            evens.append(i)

    return evens

    # without enumerate
    evens = []

    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            evens.append(i)

    return evens



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "Passed tests"