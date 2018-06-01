def string_compression(str1):
    """
    >>> string_compression("abcdefg")
    'abcdefg'

    >>> string_compression("aabcccccaaa")
    'a2b1c5a3'

    >>> string_compression("aaabbccccccaaabb")
    'a3b2c6a3b2'

    >>> string_compression("aabbccdd")
    'aabbccdd'

    >>> string_compression("")
    ''

    """

    # initialize a count variable
    # initialize a current variable to be the first letter in the string
    # make an empty list called counts which you will append things to and join
    # at the end
    # loop through each letter in the string
    # if the ltter equals the current, increment count by 1
    # if the letter does not equal current, append the current and count to the list
    # reset current to the new current letter
    # reset count to 1
    # at the end, we must append the current and the count of the final value
    # return the .joined() version of the count

    count = 0

    current = str1[0]

    counts = []

    print str1

    for letter in str1:
        if letter == current:
            count += 1

        else:
            counts.append(current)
            counts.append(str(count))
            current = letter
            count = 1

    counts.append(letter)
    counts.append(str(count))

    return "".join(counts)




print string_compression("abcccdefg")


