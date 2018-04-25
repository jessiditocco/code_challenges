class ParenStack(object):
    """A class for making a parentheses stack"""

    def __init__(self):
        self.parens = []

    def push(self, item):
        """Appends an item onto the top of the stack."""

        self.parens.append(item)

    def pop(self):
        """Removes an item from the top of the stack."""

        return self.parens.pop()

    def peak(self):
        """Returns the item at the top of the stack"""

        return self.parens[-1]

    def is_empty(self):
        """Returns True if the stack and empty and False if it isn't"""

        return not self.parens


def has_balanced_parens(phrase):
    """Does a string have balanced parentheses?
    >>> has_balanced_parens("()")
    True

    >>> has_balanced_parens("(Oh Noes!)(")
    False

    >>> has_balanced_parens("((There's a bonus open paren here.)")
    False

    >>> has_balanced_parens(")")
    False

    >>> has_balanced_parens("(")
    False

    >>> has_balanced_parens("(This has (too many closes.) ) )")
    False

    >>> has_balanced_parens("Hey...there are no parens here!")
    True

    """

    open_parens = ParenStack()

    for char in phrase:
        if char == "(":
            open_parens.push(char)
        elif char == ")":
            if open_parens.is_empty():
                return False
            else:
                open_parens.pop()

    return open_parens.is_empty()


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "Alll test passed!!!"
      
