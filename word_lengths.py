def word_lengths(sentence):
    """Get dictionary of word-length: {words}.
    >>> answer = word_lengths("cute cats chase fuzzy rats")

    >>> sorted(answer.keys())
    [4, 5]

    >>> answer[4] == {'cute', 'cats', 'rats'}
    True

    >>> answer[5] == {'chase', 'fuzzy'}
    True

    >>> answer = word_lengths("Hi, I'm Balloonicorn")

    >>> sorted(answer.keys())
    [3, 12]

    >>> answer[3] == {'Hi,', "I'm"}
    True

    >>> answer[12] == {"Balloonicorn"}
    True
    """

    # initialize a dictionary called word lengths
    # split the sentance on space
    # iterate through the split sentence list and find the length of the word
    # if the legnth of the word is a key in the dictionary, add that word
    # to the set
    # if the length of that word is not a key in the dictionary, 
    # make that length a key in the dictionary and set the value equal to 
    # a set containing that word
    # return the dictionary

    word_lengths = {}

    words = sentence.split(" ")

    for word in words:
        length = len(word)

        if length in word_lengths:
            word_lengths[length].add(word)
        else:
            word_lengths[length] = {word,}

    return word_lengths


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "Passed all tests!"