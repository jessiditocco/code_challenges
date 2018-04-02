####################### Recursion: Counting ###################################

def count():
    """Print numbers from 1 to 3"""

    num = 1

    while num < 4:
        print num

        num += 1


def count_rec(n=1):
    """Print numbers from 1 to 3 using recursion"""

    if n > 3:
        return

    print n
    count_rec(n + 1)


# count_rec()

def count_rec_more(n=1):
    """Prints numbers from 1 to 3 and back to 1"""

    if n > 3:
        return 

    print n
    count_rec_more(n + 1)
    print n


# count_rec_more()

################## Recursion: Finding Length of a List using Recursion ##################


def lenlistrec(lst):
    """Returns the length of the list using recursion."""

    if not lst:
        return 0
    
    return 1 + lenlistrec(lst[1:])


# print lenlistrec(["apple", "berry", "cherry"])


##################  Doubler without Recursion ##################
# For every item in a list, print the value doubled

def doubler(lst):
    """prints double each value in the list"""

    for n in lst:
        print n * 2


# What if we have something like this though== we need to flatten them out and still print
# [1, [2, [3], 4], 5]
# We can do this without recursion using a stack:

def doubler_no_recursion(lst):
    """Prints items in a list doubled, not using recursion."""

    stack = list(reversed(lst))

    while stack:
        n = stack.pop()

        # isintance(object, classinfo)
        # if the object is the type that you pass in for classinfo, returns true
        if isinstance(n, list):
            # If its a list, add it to the stack, reversed
            for inner in reversed(n):
                stack.append(inner)
        else:
            print n * 2

    # While this solution is pretty hairy, this solution uses a stack
    # Because we are adding new wowrk to the end and popping them off the end

# doubler_no_recursion([1, [2, [3], 4], 5])


################################ Doubler with Recursion ##########################

def doubler_using_rec(lst):
    """Prints items in a list, doubled, using recursion."""

    # Loop through each item in the list
    # If the item we are on is a list, we want to recurse and call the function doubler
    # On that list
    # If the item we are on is an number, we want to print double that number

    for x in lst:
        if isinstance(x, list):
            doubler_using_rec(x)

        else:
            print x * 2

doubler_using_rec([1, [2, [3], 4], 5])



################################ Recursively LS from Tree (Filesystem) ##########################

class Node(object):
    """Node in a tree."""

    def __init__(self, data, children=None):
        self.data = data
        self.children = children or []

# Using recursion, its easy to implement depth first search
def ls(node):
    """prints items in tree form this node."""

    print node.data

    for child in node.children:
        ls(child)


resume = Node("resume.txt")
recipes = Node("recipes.txt")
jane = Node("jane/", [resume, recipes])
server = Node("server.py")
jessica = Node("jessica/", [server])
users = Node("users/", [jane, jessica])
root = Node("/", [users])



