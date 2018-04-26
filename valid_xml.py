class xmlStack(object):
    def __init__(self):
        self.xml = []

    def pop(self):
        return self.xml.pop()

    def push(self, item):
        self.xml.append(item)

    def peak(self):
        return self.xml[-1]

    def is_empty(self):
        return not self.xml


def is_valid_xml(str):
    """Returns True if the input is valid xml
    >>> is_valid_xml("<a></a>")
    True

    >>> is_valid_xml("<a><b></b></a>")
    True

    >>> is_valid_xml("<a><b></b><c></c></a>")
    True

    >>> is_valid_xml("<a></b><b></a>")
    False

    >>> is_valid_xml("<a><b></a></b>")
    False

    """
    
    # generate a function that takes in a string
    # make a stack to keep tack of open xml tags
    # loop through the string and slice 0:2 --> every 3 charecters
    # if it is an opening xml, append it to the stack
    # if its a closing xml (so it has a slash)
    # make sure that the stack is not emtpy --> if it is, return false
    # if its a match to the top of the stack, pop off the stack
    # else, return false

    # if we get to the end of the string, and our stack is empty, return True

    opening_tags = xmlStack()

    for i, char in enumerate(str):
        # if the charecter is a valid alphabetic letter and the 
        # charecter at the index right before the charecter that
        # i am on is not a back tag (aka we aren't dealing with a closing)
        # tag, we want to push it onto the stack
        if char.isalpha() and str[i - 1] != "/":
            opening_tags.push(char)

        elif char.isalpha and str[i - 1] == "/":
            # if the charecter is a valid alphabetic letter
            # and the charecter at the index before the charecter that
            # i am on is a back slash.. it is a closing tag

            # to fail fast: if the stack is emtpy, return False
            if opening_tags.is_empty():
                return False
            # if the charecter is equal to the charecter at the top of the stack
            # pop off the stack
            elif char == opening_tags.peak():
                opening_tags.pop()

            else:
                return False

    if opening_tags.is_empty():
        return True


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All tests passed!"



