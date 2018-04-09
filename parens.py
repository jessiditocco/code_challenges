"""Checking to see if parenthesis are balanced with a stack."""

class Stack(object):
    """A simple stack class implemented using a list."""

    def __init__(self):
        self.data = []


    def push(self, item):
        """Appends an item to the stack."""

        self.data.append(item)

    def pop(self):
        """Removes an item from the top of the stack."""

        return self.data.pop()


    def peak(self):
        """Shows the next item at the top of the stack."""

        return self.data[-1]


    def is_empty(self):
        """Boolean expression to check if the next item in the stack is empty."""

        return not self.data


# Loop through each item in the string
# If the item is an open parenthesis, add it to the stack
# If the item is a closed paren, 
    # If the stack is not empty,
    # pop from the stack
    # If the stack is empty and we cant pop from the stack, we want to return False



def are_parens_balanced(paren_string):
    """Returns a boolean expression that tells whether the parenthesis are balanced in an expression

    >>> are_parens_balanced("((3+4) - (1+2))/(1+1)")
    True

    """

    parens_stack = Stack()

    for char in paren_string:
        if char == "(":
            # If the character is an open quote, push it onto the stack
            parens_stack.push(char)

        elif char == ")":
            if parens_stack.is_empty():
                # If the paren stack is empty, that means we don't
                # Have a balanced expression of parens 
                return False

            else:
                parens_stack.pop()

    return True


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "yay! Passed the test."


