class Stack(object):
    def __init__(self):
        self.brackets = []

    def __repr__(self):
        return "<{}>".format([item for item in self.brackets])

    def push(self, item):
        self.brackets.append(item)

    def pop(self):
        return self.brackets.pop()

    def is_empty(self):
        return not self.brackets

    def peak(self):
        return self.brackets[-1]

def has_balanced_brackets(phrase):
    """Does a given string have balanced pairs of brackets?

    Given a string as input, return True or False depending on whether the
    string contains balanced (), {}, [], and/or <>.

    >>> has_balanced_brackets("<ok>")
    True

    >>> has_balanced_brackets("<[ok]>")
    True

    >>> has_balanced_brackets("<[{(yay)}]>")
    True

    >>> has_balanced_brackets("(Oops!){")
    False

    >>> has_balanced_brackets("{[[This has too many open square brackets.]}")
    False

    >>> has_balanced_brackets(">")
    False

    >>> has_balanced_brackets("(This has {too many} ) closers. )")
    False

    >>> has_balanced_brackets("<{Not Ok>}")
    False

    >>> has_balanced_brackets("No brackets here!")
    True
    """

    # make a dictionary where we can look up the closers to openers
    
    closers_to_openers = {")": "(", "]": "[", "}": "{", ">": "<"}


    # make a set of all of the opener charecters, used to match openers quickly

    openers = set(closers_to_openers.values())

    # create an empty list to use as a stack
    openers_seen = Stack()

    # loop through
    for char in phrase:
        # Push open brackets onto the stack if they are openers
        if char in openers:
            openers_seen.push(char)

        # If the charecter is not an opener
        # Check to see that the charecter is a closer

        # If the closer doesn't have an opener at all, return False
        # if the closer has an opener, but its not its match, return False
        # if the closer has an opener that is its match, pop off the end of openers
        # seen
        # if we get to the end of the loop and the stack is empty, we return True

        elif char in closers_to_openers:
            if openers_seen.is_empty():
                return False
            if openers_seen.peak() == closers_to_openers.get(char):
                openers_seen.pop()
            else:
                return False

    return openers_seen.is_empty()

    # open_brackets = Stack()

    # bracket_pairs = {"(": ")", "{": "}", "[": "]", "<": ">"}
    # # in order to optimize runtime, we can make a set out of the bracket pair
    # # values so that we are looking up in a set rather than a list which would
    # # make the runtime O(N^2)
    # closing_brackets = set(bracket_pairs.values())


    # for char in phrase:
    #     if char in bracket_pairs:
    #         open_brackets.push(char)

    #     elif char in closing_brackets:
    #         # We must check to make sure that the open brackets isn't empty
    #         # If it was empty and we didn't have this statment to exit out of the loop
    #         # we would get an list index out of range when we tried to run peak()
    #         if open_brackets.is_empty():
    #             return False
    #         elif char == bracket_pairs[open_brackets.peak()]:
    #             open_brackets.pop()
    #         elif char != bracket_pairs[open_brackets.peak()]:
    #             return False

            
    # return open_brackets.is_empty()





if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All tests passed!"

