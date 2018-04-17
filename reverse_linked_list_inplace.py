class Node(object):
    """Class in a linked list."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList(object):
    """Linked list."""

    def __init__(self, head=None):
        self.head = head

    def as_string(self):
        """Represent data for this list as a string.

        >>> LinkedList(Node(3)).as_string()
        '3'

        >>> LinkedList(Node(3, Node(2, Node(1)))).as_string()
        '321'
        """

        out = []
        n = self.head

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(out)



def reverse_linked_list_in_place(lst):
    """Given linked list, reverse the nodes in this linked list in place.

    >>> ll = LinkedList(Node(1, Node(2, Node(3))))

    >>> reverse_linked_list_in_place(ll)

    >>> ll.as_string()
    '321'

    """

     # initlize a variable called previous-- keep track of the one we were on
     # previous will start with None
     # initialize a variable called current-- current will start at the current tail
     # loop through using a while loop:
     # while current is not none
     # Update the currents next to previous
     # Increment current to be the next value
     # Exit the loop and reassign the head to the current value

    previous = None
    current = lst.head

    while current is not None:
        next = current.next
        current.next = previous
        previous = current
        current = next
        

    lst.head = previous


    # initialize a variable called previous 
    # start a while loop: while current is not none
    # current will start as the lists head
    # reassign current to the next item
    # previous is equal to the current
    # repoint the list head



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All tests passed!!! Wooo"