# Given an integer n, return a list containing n unique random numbers between 1-10, inclusive. (That is, do not repeat any numbers in the returned list.)

# You can trust that this function will never be called with n < 0 or n > 10.

import random

def lucky_numbers(n):
    """Return n unique random numbers from 1-10 (inclusive).
    >>> lucky_numbers(2)
    [3, 7]

    >>> lucky_numbers(0)
    []

    >>> sorted(lucky_numbers(10))
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """

    # create a list of numbers between one and 10
    # initialize a lucky_nums empty list 
    # for i in range(n)
    # pick a random number from the list
    # append that number to the list
    # remove that number from the list so that we cant choose it again
    # return the list


    nums = range(1, 11)
    lucky_nums = []

    for i in range(n):
        random_num = random.choice(nums)
        lucky_nums.append(random_num)
        nums.remove(random_num)

    return lucky_nums 





if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == None:
        print "ALL TESTS PASSED!!"
