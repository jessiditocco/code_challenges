def word_count(phrase):
    """Count words in a sentence, and print in ascending order.

    >>> word_count("berry cherry cherry cherry berry apple")
    apple: 1
    berry: 2
    cherry: 3

    >>> word_count("hey hi hello")
    hello: 1
    hey: 1
    hi: 1

    >>> word_count("hi Hi hi")
    Hi: 1
    hi: 2
    """
    # initialize a word_count dictionary
    # loop through each word in the string and use .get() to add item
    # count to the dictionary

    # for items in sorted(items), print the word and the count

    # dictionaries are inherently unordered... you cant do
    # animals.sort()
    # however.. you can do sorted(animals)-- this will turn the keys
    # into a list and sorts the keys

    word_count = {}
    phrase = phrase.split(" ")

    for word in phrase:
        word_count[word] = word_count.get(word, 0) + 1

    for item in sorted(word_count.items()):
        print "{}: {}".format(item[0], item[1])




# word_count("berry cherry cherry cherry berry apple")
word_count("hey hi hello")

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All tests passed"


