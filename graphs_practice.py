############################ Node and Graph Class ##############################

class PersonNode(object):
    """Node in a graph representing a person."""

    def __init__(self, name, adjacent=None):
        """Create a person node with friends adjacent."""
        
        self.name = name

        if adjacent:
            # Assert condition: youer telling the program to test that condition and
            # Trigger an error if the condition is false
            # So, if a set is passed in, then we set self.adjacent to that set
            # Nothing will happen in the assert statment
            # But.. if we pass in something other than a set, the assert statement 
            # Will return "adjacent must be a set" warning
            assert isinstance(adjacent, set), "adjacent must be a set!"
            self.adjacent = adjacent

            # if nothing is passed in for adjacent.. we will set self.adjacent to an empty set
        else:
            self.adjacent = set()

############## Queue Class #######################

class Queue(object):
    """Simple FIFO queue, implemented using a list.

    This is a non-optimal way to make a queue--but it's just here as a demo
    of using a queue. Much better would be to use a linked list or
    collections.deque.
    """

    def __init__(self):
        self._data = []

    def enqueue(self, node):
        """Add item to end of queue."""

        self._data.append(node)

    def dequeue(self):
        """Remove item from start of queue and return."""

        return self._data.pop(0)

    def is_empty(self):
        """Is the queue empty?"""

        return not self._data

    def peek(self):
        """Return (but don't pop!) first item from start."""

        return self._data[0]

############## Friend Graph #######################

class FriendGraph(object):
    """Graph holding people and their friendships"""

    def __init__(self):
        """Creates an empty graph."""

        self.nodes = set()

    def __repr__(self):
        return "<FriendGraph: {}".format([n.name for n in self.nodes])


    def add_person(self, person):
        """Add a person to our graph"""

        self.nodes.add(person)

    def add_people(self, people_list):
        """Add a list of people to our graph"""

        for person in people_list:
            self.add_person(person)

    def set_friends(self, person1, person2):
        """Set two people as friends"""

        person1.adjacent.add(person2)
        person2.adjacent.add(person1)

    def are_connected(self, person1, person2):
        """Are two people friends? Breadth-first search."""

        # to_visit could also be a set
        to_visit = Queue()

        to_visit.enqueue(person1)
        seen = set()
        seen.add(person1)

        while not to_visit.is_empty():
            current = to_visit.dequeue()
            print "checking {}".format(current)

            if current is person2:
                return True

            else:
                for friend in current.adjacent - seen:
                    to_visit.enqueue(friend)
                    seen.add(friend)
                    print "added to queue {}".format(friend)

        return False
# This is a breadth first search... it would be a (depth-first search if we used a stack)


    def are_connected_recursive(self, person1, person2, seen=None):
        """Are two people friends? Recursive depth-first search."""

        if not seen:
            seen = set()

        if person1 is person2:
            return True

        # Keep track of what we have visited
        seen.add(person1)

        for person in person1.adjacent - seen:
            if self.are_connected_recursive(person, person2, seen):
                return True

        return False


if __name__ == "__main__":
    # If we run this file directly..
    # Add sample friends
    harry = PersonNode("Harry")
    hermione = PersonNode("Hermione")
    ron = PersonNode("Ron")
    neville = PersonNode("Neville")
    trevor = PersonNode("Trevor")
    fred = PersonNode("Fred")
    draco = PersonNode("Draco")
    crabbe = PersonNode("Crabbe")
    goyle = PersonNode("Goyle")

    hogwarts = FriendGraph()
    hogwarts.add_people([harry, hermione, ron,
                        neville, fred, trevor,
                        draco, crabbe, goyle])

    hogwarts.set_friends(harry, hermione)
    hogwarts.set_friends(harry, ron)
    hogwarts.set_friends(harry, neville)
    hogwarts.set_friends(hermione, ron)
    hogwarts.set_friends(neville, hermione)
    hogwarts.set_friends(neville, trevor)
    hogwarts.set_friends(ron, fred)
    hogwarts.set_friends(draco, crabbe)
    hogwarts.set_friends(draco, goyle)
