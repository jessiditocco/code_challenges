def has_unique_chars(word):
    """Does word contains unique set of characters?
    >>> has_unique_chars("Monday")
    True

    >>> has_unique_chars("Moonday")
    False

    >>> has_unique_chars("")
    True

    >>> has_unique_chars("Bob")
    True
    """

    # Given a word, return True if that word contains only unique characters. Return False otherwise.

    # initialize a dict
    # loop through charecters in a word and update dict count
    # loop through the counts in the dict and if any count is more than 1 return false
    # else return true
    # runtime will be 0(n)

    # letter_counts = {}

    # for letter in word:
    #     letter_counts[letter] = letter_counts.get(letter, 0) + 1

    # for value in letter_counts.values():
    #     if value > 1:
    #         return False

    # return True

    # With a set:
    # make a set of the charecters
    # if the length of the set is not equal to the length of the word:
        # return False
    # Making a set takes O(n) time

    unique_letters = set(word)

    return len(unique_letters) == len(word):


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "all tests passed!"