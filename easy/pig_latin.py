# Write a funtion to turn a phrase into Pig Latin


def pig_latin(phrase):
    """Turn a phrase into pig latin.

    There will be no uppercase letters or punctuation in the phrase.

    >>> pig_latin('hello awesome programmer')
    'ellohay awesomeyay rogrammerpay'
    
    >>> pig_latin('porcupines are cute')
    'orcupinespay areyay utecay'

    >>> pig_latin('give me an apple')
    'ivegay emay anyay appleyay'

    """


    words = phrase.split()
    pig_latin = []

    for word in words:
        if word[0] in "aeuiou":
            word = word + "yay"
            
        else:
            word = word[1:] + word[0] + "ay"

        pig_latin.append(word)

    return " ".join(pig_latin)

if __name__ == "__main__":
    import doctest
    doctest.testmod()