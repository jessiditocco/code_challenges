def print_astericks(num, stars="*"):
    """Print astericks in order of one star to the number using recursion
    print_astericks(5)
    >>> *
        **
        ***
        ****
        *****
    """

    # basecase: return None if the number is zero
    # print stars
    # concatenate a new star to the end of stars and pass it into the function
    # call the function with number decremented by 1 each time
    # and the new stars


    if num == 0:
        return

    print stars
    stars = stars + "*"

    return print_astericks((num - 1), stars)


print_astericks(2)
