"""Stack implemented using Python list"""

class StackEmptyError(IndexError):
    """Attempt to pop an empty stack."""


class Stack(object):
    """LIFO stack.

    Implemented using a Python list; since stacks just need
    to pop and push, a list is a good implementation as popping
    and appending to the end of a list is an O(1) operation. However,
    in cases where performance matters, it might be best to use
    a Python list directly, becuase it avoids the overhead of a custom class.

    For even better performance and for a smalller memory footprint,
    you can use the collections.deque object, which can act like a 
    stack. 

    We could also write our own linkedlist class for a stack, where we push
    things onto the head and pop things off the head (effectively reversing it),
    but that would be less efficient than using a built-in Python list or a collections.deque
    object.
    """

    def __init__(self, inlist=None):
        if inlist:
            self._list = inlist

        else:
            self._list = []


    def __repr__(self):
        if not self._list:
            return "<Stack (empty)"

        else:
            return "<Stack tail={} length={}".format(self._list[-1], len(self._list))

    def push(self, item):
        """Adds an item to the end of the stack."""

        self._list.append(item)


    def pop(self):
        """Removes an item from the end of the stack and returns the item."""

        # Ensure that the list is not empty
        # if it is, raise the stack empty error

        if not self._list:
            raise StackEmptyError

        return self._list.pop()

    def length(self):
        """Returns length of stack."""

        return len(self._list)


    def peak(self):
        """Returns the top item in the stack."""

        return self._list[-1]


    def empty(self):
        """Empty the stack"""

        self._list = []

    def is_empty(self):
        """Is the stack empty?"""

        return not self._list

### Pancake shop

class PancakeStack(Stack):
    """A stack of pancakes."""

    def __repr__(self):
        """A representation of the Pancake stack."""

        return "<PancakeStack NEXT: {pancake} REMAINING: {num}".format(


    def eat_next_pancake(self):
        """Remove a pancake from the stack."""

        print "MMM {} pancakes are tasty.".format(self.pop())


    def empty(self):
        """Clear all of the pancakes from the plate."""

        while not self.is_empty():
            print "There goes the {} pancake".format(self.pop())

        self.print_empty_plate()


    def check_next_pancake(self):
        """Display the pancake at the top of the stack."""

        next_pancake = self.peak()

        if next_pancake:
            print "The next pancake in the stack is a {} pancake".format(next_pancake)

        print self.print_empty_plate()


    def check_plate(self):
        """Print an ASCII-art representation of the pancake stack."""

        if not self.is_empty():
            print
            print "     ({})        <--top of stack".format(self._list[-1])
            for pancake in self._list[-2:-1]:
                print " {} ".format(pancake)
            print "\________________________/"
            print


    def print_empty_plate(self):
        """ascii representation of pancake plate without pancakes"""


        print
        print "Your plate is empty..."
        print "\________________________/"
        print


    def run_pancake_shop(pancakes=None):
        """REPL (read, evaluate, print loop) for our pancake dinner."""

        if pancakes:
            plate = PancakeStack(pancakes)

        else:
            plate = PancakeStack()


        print "Welcome to the pancake shop"

        while True:
            print "Do you want to: "
            print "O)rder a pancake, E)at a pancake, C)heck your plate, or L)eave?"
            user_input = raw_input("> ").upper()

            if user_input == "O":
                flavor = raw_input("What flavor pancake would you like? ")
                plate.push(flavor)

            elif user_input == "E":
                plate.eat_next_pancake()

            elif user_input == "C":
                plate.check_plate()

            elif user_input == "L":
                print "Have a nice day!"
                break
            else:
                print "That is not one of the options, please try again."
