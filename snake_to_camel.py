def snake_to_camel(variable_name):
    """Given a variable name in snake_case, return camelCase of name.

    >>> snake_to_camel("hi_balloonicorn")
    'hiBalloonicorn'
    """

    # split the string on the underscore
    # loop through the words in the list from the 1st index (excluding 0)
    # and capitlaize the first letter
    # join the list and return it


    split = variable_name.split("_")

    # in order to capture this, we must reassign the capitalized word
    # in the list

    for i in range(1, len(split)):
        split[i] = split[i].capitalize()

    return "".join(split)


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "Passed all tests!"