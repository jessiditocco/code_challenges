def is_pangram(sentence):
    """Given a string, return True if it is a pangram, False otherwise.

    >>> is_pangram("The quick brown fox jumps over the lazy dog!")
    True

    >>> is_pangram("I like cats, but not mice")
    False

    """

    # a panagram is a sentence that contains all of the letters of the english
    # alphabet at least once

    # create a set out of the sentence
    # create a set out of the english dictionary (make sure to add a space)
    # check to see that the sets are equal
    # if so, return True

    # english_dict = {" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}

    # char_count = {}

    # for char in sentence:
    #     char_count[char] = char_count.get(char, 0) + 1

    # for item in english_dict:
    #     if item not in char_count.keys():
    #         return False

    # return True

    # we can use a set comprehension...
    # loop through the charecters in the sentence
    # if the charecter is_alpha(not a space)...
    # add it to the set (lowercased)

    seen = set()

    for char in sentence:
        if char.isalpha():
            seen.add(char.lower())

    return len(seen) == 26



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All tests passed!!"


