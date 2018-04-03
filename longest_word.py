def find_longest_word(words):
    """Return longest word in list of words.

    >>> find_longest_word(["hi", "hello"])
    5

    >>> find_longest_word(["Balloonicorn", "Hackbright"])
    12

    """

    longest_word_length = len(words[0])

    for word in words:
        if len(word) > longest_word_length:
            longest_word_length = len(word)

    return longest_word_length

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All tests passed! Wooo!"