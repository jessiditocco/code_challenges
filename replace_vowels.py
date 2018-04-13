def replace_vowels(chars):
    """Given list of chars, return a new copy, but with vowels replaced by '*'.
    >>> replace_vowels(['h', 'i'])
    ['h', '*']

    >>> replace_vowels(['o', 'o', 'o'])
    ['*', '*', '*']

    >>> replace_vowels(['z', 'z', 'z'])
    ['z', 'z', 'z']

    >>> replace_vowels([])
    []

    >>> replace_vowels(["A", "b"])
    ['*', 'b']

    >>> replace_vowels(["y", "a", "y"])
    ['y', '*', 'y']

    """

    # given a list of charecters, return a new copy but with
    # vowels replaced by *

    # make a set of vowels
    # iterate through the items in the list and if the charecter
    # is in the vowel set, replace the vowel with a star

    vowels = {"a", "e", "i", "o", "u"}
    replaced = []

    # return ["*" if char in vowels else char for char in chars]

    for char in chars:
        if char.lower() in vowels:
            replaced.append("*")

        else:
            replaced.append(char)

    return replaced

    


    # The runtime for this function should be O(n)
    # We optimize by using a set instead of a list for the vowels
    # becuase lookup in a set is O(1) where as lookup in a list is O(n)



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All tests passed"
