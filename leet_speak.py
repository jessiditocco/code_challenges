def translate_leet(phrase):
    """Translates input into "leet-speak".
    >>> translate_leet("Hi Balloonicorn")
    'Hi B@1100nic0rn'

    >>> translate_leet("Hackbright is the Shizzle")
    'H@ckbrigh7 i5 7h3 5hizz13'
    """

    english_to_leet_conversion = {"a": "@", "o": "0", "e": "3", "l": "1", "s": "5", "t" : "7"}

    translated = ""

    # Loop through each letter in the phrase
    # use .get to get the value of the key at the lower- cased version of the letter
    # If that doesn't exist, give the letter
    # increment the translated string by this character
    for letter in phrase:
       translated += english_to_leet_conversion.get(letter.lower(), letter)

    return translated

# It might feel like the runtime of this code is linear time, o(n) since we are
# looping over each charecter...
# But notice what we do in the loop... we look up in the dict (constant time)
# and we also concatenate the letter to the string
# this later part might feel like constant time but it isn't...
# strings are immutable in python... so you are never really adding to a string
# instead.. you are building up a new string which gets longer every time
# making a 5-charecter long string is 5 times as much work as making a 1 char long string
# RUNTIME IS ACTUALLY o(n**2)


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "Alll tests passed!!!!"



