def concat_lists(list1, list2):
    """Combine lists.

    >>> concat_lists([1, 2], [3, 4])
    [1, 2, 3, 4]

    >> > concat_lists([], [1, 2])
    [1, 2]

    >>> concat_lists([1, 2], [])
    [1, 2]

    >>> concat_lists([], [])
    []
    """

    # return list1 + list2
    for item in list2:
        list1.append(item)

    return list1


if __name__ == "__name__":
    import doctest
    doctest.testmod()