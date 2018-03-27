def is_prime(num):
    """Is a number a prime number?
    >>> is_prime(0)
    False

    >>> is_prime(1)
    False

    >>> is_prime(2)
    True

    >>> is_prime(3)
    True

    >>> is_prime(4)
    False

    >>> is_prime(11)
    True

    >>> is_prime(999)
    False
    """

# Write a function the returns True or False, depending on whether the integer 
# passed into it is a prime number.

# Only numbers >1 can be prime numbers:
    
    # if number < 2,return False

    # loop through each number from 2 to the the number minus 1

    # if the number to check / number is equal to zero, return false

    # else return true

    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All tests passed!!!"

