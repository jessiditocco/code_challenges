def primes(count):
    """Return count number of prime numbers, starting at 2.
   
    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]

    """

    # initialize an empty list called primes
    # initialize a variable called number starting at 2
    # while the length of the list is less than count
    # if number is 2, append it to the list
    # check if number is prime (function)
    # if it is, add it to the list
    # increment the number variable

    primes = []

    current_number = 2

    while len(primes) < count:
        if current_number == 2:
            primes.append(current_number)

        elif is_prime(current_number):
            primes.append(current_number)

        current_number += 1

    return primes


def is_prime(number):
    """Checks if a number is prime"""

    for num in range(2, number):
        if number % num == 0:
            return False

    return True


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "all tests passed!!!"