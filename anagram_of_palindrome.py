# Anagram of Palindrome

# Is the word an anagram of a palindrome?


def is_anagram_of_palindrome(str):
    """ 
        >>> is_anagram_of_palindrome("a")
        True

        >>> is_anagram_of_palindrome("ab")
        False

        >>> is_anagram_of_palindrome("aab")
        True

        >>> is_anagram_of_palindrome("arceace")
        True

        >>> is_anagram_of_palindrome("arceaceb")
        False
    """
    # make a dict of the letter counts
    # initializing a dictionary is o(1)
    letter_count = {}

    # Loop through each letter and increment the dictionary accordingly
    # o(n) looping through each character in string
    for char in str:
        letter_count[char] = letter_count.get(char, 0) + 1 #o(1)

    odd_letter_count = 0 #o(1)

    for char in letter_count: #o(n)
        if letter_count[char] % 2 != 0: 
            odd_letter_count += 1

    if odd_letter_count > 1:
        return False
    else:
        return True

# overall runtime is o(2n) --> o(n)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
