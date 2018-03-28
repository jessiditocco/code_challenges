# create a stack class and then implement an algorithm to check whether parenthesis are balanced

class Stack(object):
    """Stack using a list and LIFO"""

    def __init__(self, stack=None):
        if not stack:
            self.stack = []
        else:
            self.stack = stack

    def push(self, item):
        """Adds an item to the top of the stack"""

        self.stack.append(item)


    def pop(self):
        """Removes an item from the top of the stack"""

        return self.stack.pop()

    def peak(self):
        """Returns the top item in the stack."""

        print self.stack[-1]

    def is_empty(self):
        """Checks whether the stack is empty"""

        return not self.stack



def are_parens_balanced(symbols):
    """Are parenthesis balanced in the expression?
    
    >>> are_parens_balanced("((3+4) - (1+2))/(1+1)")
    True

    """

    # make a parenthesis stack
    # loop through the symbols, if the charecter is open paren, push it onto the stack
    # if the parenthsis is a closing paren, pop it from the stack

    parens = Stack()

    for char in symbols:
        if char == "(":
            parens.push("(")

        elif char == ")":
            if parens.is_empty():
                return False
            else:
                parens.pop()

    return parens.is_empty()

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All tests passed!! wahooo!"

################### Practice using the collections library ######################
# import collections

# dq = collections.deque()

# dq.append("hi")
# print dq
# dq.append("hackbright")
# print dq
# dq.pop()

# dq.append("hellow")
# print dq

# dq.popleft()
# print dq

## Collections is used so that you dont have to implement your own stack or queue
## Collections lib uses doubly linked lists and you can treat it as either  a stack or a queue
