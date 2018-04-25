# Binary Search

def binary_search(val):
    """Using binary search, find val in range 1-100. Return # of guesses
        >>> binary_search(50)
        1

        >>> binary_search(25)
        2

        >>> binary_search(75)
        2

        >>> binary_search(31) <= 7
        True

        >>> max([binary_search(i) for i in range(1, 101)])
        7
    """

    assert 0 < val < 101, "Value must be between 1 and 100"

    num_guesses = 0

    lower_bound = 0
    upper_bound = 101

    # start the while loop
    while True:
        # Increment number of guesses by 1
        num_guesses += 1

        midpoint = (lower_bound + upper_bound) / 2

        if midpoint == val:
            return num_guesses
        elif midpoint > val:
            upper_bound = midpoint
        elif midpoint < val:
            lower_bound = midpoint





  #   # ensure that the value is between 1-100
  #   assert 0 < val < 101, "Val must be between 1-100"

  #   # initialize right, left bounds and num guesses outside of loop
  #   # o(1) for initializing a var
  #   left_bound = 0
  #   right_bound = 101
  #   num_guesses = 0

  #   # initiate a while loop
    
  #   while True:
  #       # increment the number of guesses by 1
  #       num_guesses += 1
  #       # find the midpoint of the right and left bounds
  #       midpoint = (right_bound + left_bound) / 2
  #       # if the midpoint is equal to the value, return number of guesses 
  #       if midpoint == val:
  #           return num_guesses
  #       # if not, adjust the right and left bound accordingly
  #       elif midpoint > val:
  #           right_bound = midpoint
  #       else:
  #           left_bound = midpoint


  # # o(log n) runtime because for each time through the loop we reduce our
  # # range that the number could be in by half


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print 'All tests passed!'
