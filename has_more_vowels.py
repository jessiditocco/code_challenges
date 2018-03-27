def has_more_vowels(word):
    """Does word contain more vowels than non-vowels?
    >>> has_more_vowels("moose")
    True
    >>> has_more_vowels("mice")
    False

    >>> has_more_vowels("graph")
    False

    >>> has_more_vowels("yay")
    False

    >>> has_more_vowels("Aal")
    True
    
    """

# If the phrase is over half vowels, it should return True:

    # intialize a vowel count variable 
    # Loop through the letters of the word:
    # if the letter is in the set of vowels, increment the vowel count
    # if vowel count is greater than length of the word divided by 2, return True
    # else return false


    vowel_count = 0

    for letter in word:
        if letter.lower() in {"a", "e", "i", "o", "u"}:
            vowel_count += 1

    if vowel_count > (len(word) / 2):
        return True

    return False

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All tests passed!!!"