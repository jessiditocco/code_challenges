class Node(object):
    """Class in a linked list."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def as_string(self):
        """Represent data for this node and it's successors as a string.

        >>> Node(3).as_string()
        '3'

        >>> Node(3, Node(2, Node(1))).as_string()
        '321'
        """

        out = []
        n = self

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(out)




def reverse_linked_list(head):
    """Given LL head node, return head node of new, reversed linked list.

    >>> ll = Node(1, Node(2, Node(3)))
    >>> reverse_linked_list(ll).as_string()
    '321'
    """

    # We need to make a temporary variable that will start with None
    # This will be our new tails next (none) and we will update it with each previous
    # Node as we loop through
    # We will iterate through the entire linked list (while n)
    # We will create a new Node with data from the current node that we are on and 
    # The next, being the previous node that we were on
    # Then we will increment our head n to move forward

    node_for_reversing = None

    n = head

    while n:
        node_for_reversing = Node(n.data, node_for_reversing)
        n = n.next

    return node_for_reversing


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "Tests passed!!!!"