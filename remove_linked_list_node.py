class Node(object):
    """Node class for a linked list."""

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

        current = self
        nodes = []

        while current is not None:
            nodes.append(str(current.data))
            current = current.next

        return "".join(nodes)


def remove_node(node):
    """Given a node in a linked list, remove it.

    Remove this node from a linked list. Note that we do not have access to
    any other nodes of the linked list, like the head or the tail.

    Does not return anything; changes list in place.
    """

    # We cannot remove the last node, only the first node or one in the middle
    # we can cleverly reassign the Node that we are trying to delete to have 
    # data attribute equal to the next nodes data atttribute
    # and next attribute to the next, next's

    if not node.next:
        raise ValueError("You cannot remove the last node!")

    node.data = node.next.data
    node.next = node.next.next

    # The runtime of this is O(1)


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All tests passed!!"

