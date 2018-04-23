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
    
    # closers_to_openers = {")": "(", "]": "[", "}": "{", ">": "<"}


    # # make a set of all of the opener charecters, used to match openers quickly

    # openers = set(closers_to_openers.values())

    # # create an empty list to use as a stack
    # openers_seen = Stack()

    # # loop through
    # for char in phrase:
    #     # Push open brackets onto the stack if they are openers
    #     if char in openers:
    #         openers_seen.push(char)

    #     # If the charecter is not an opener
    #     # Check to see that the charecter is a closer

    #     # If the closer doesn't have an opener at all, return False
    #     # if the closer has an opener, but its not its match, return False
    #     # if the closer has an opener that is its match, pop off the end of openers
    #     # seen
    #     # if we get to the end of the loop and the stack is empty, we return True

    #     elif char in closers_to_openers:
    #         if openers_seen.is_empty():
    #             return False
    #         if openers_seen.peak() == closers_to_openers.get(char):
    #             openers_seen.pop()
    #         else:
    #             return False

    # return openers_seen.is_empty()


    closers_to_openers = {")": "(", "]": "[", "}": "{", ">": "<"}

    openers = set(closers_to_openers.values())
    closers = set(closers_to_openers.keys())

    openers_seen = Stack()

    for char in phrase:
        if char in openers:
            openers_seen.push(char)

        elif char in closers:
            if openers_seen.is_empty():
                return False
            elif char == closers_to_openers[openers_seen.peak()]:
                openers_seen.pop()
            else:
                return False

    return openers_seen == []

# has_balanced_brackets("No brackets here!")

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All tests passed!"

