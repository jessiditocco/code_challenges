def is_palindrome(word):
    """Return True/False if this word is a palindrome.

    >>> is_palindrome("a")
    True

    >>> is_palindrome("noon")
    True

    >>> is_palindrome("racecar")
    True

    >>> is_palindrome("porcupine")
    False

    >>> is_palindrome("Racecar")
    False

    """

    # # using list slicing
    # # Runtime for list slicing: a[:k] = b[:k]
    # # In this case, our runtime would be O(k) where k is the entire length of the lsit

    # if word == word[::-1]:
    #     return True

    # return False

    # using iteration
    # make a right index and a left index
    # while the right index < left index
    # if the value of the right index doesnt equal the value of the left index, return False
    # Increment left and right index
    # return True if you get all the way through the loop and all letters are equal


    # left_index = 0
    # right_index = len(word) - 1

    # while left_index < right_index:
    #     if word[left_index] != word[right_index]:
    #         return False
    #     left_index += 1
    #     right_index -= 1

    # return True 

    for i in range(len(word) / 2):
        if word[i] != word[-i - 1]:
            return False
    return True


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All test passed!!"