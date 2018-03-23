
def decode(s):
    """Decode a string.
    >>> decode("0h")
    'h'
    >>> decode("2abh")
    'h'
    >>> decode("0h1ae2bcy")
    'hey'
    """

    # loop through indices-- we will want to use indices becuase we will need to index into the word later on
    # Initialize an empty string
    
    decoded_word = ""

    # Initialize i equal to zero
    i = 0

    # While i is less than the length of the word
    while i < len(s):
        # Number to skip will only update if s[i] is an integer
        num_to_skip = int(s[i])
        # Increment i by the number to skip plus 1, which will give the index of the letter we want to add to the string
        i += num_to_skip + 1
        # Index into the string at that index to find the letter that we will add to the decoded word
        decoded_word += s[i]
        # Increment i to move on to the next letter
        i += 1

    return decoded_word



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "ALL TESTS PASSED WOOO!!!!!"