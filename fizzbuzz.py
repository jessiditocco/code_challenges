def fizzbuzz():
    """Count from 1 to 20 in fizzbuzz fashion."""

    # loop through range from 1-21
    # if the number is evenly divisible by 3 and by 5, print fizzbuzz
    # if the number divided by 3 is equal to zero but not 5, print fizz
    # if the number is evenly divisibly by 5 but not 3, print buzz
    # else print the number

    for num in range(1, 21):
        if (num % 3 == 0) and (num % 5 == 0):
            print "fizzbuzz"
        elif (num % 3 == 0):
            print "fizz"
        elif (num % 5 == 0):
            print "buzz"
        else:
            print num

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All tests passed yayy!!"