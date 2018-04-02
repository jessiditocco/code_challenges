####################### Binary Search Node ###################################

# class BinarySearchNode(object):
#     """Binary tree node."""

#     def __init__(self, data, left=None, right=None):
#         self.data = data

#         self.left = left
#         self.right = right

#     def __repr__(self):
#         """Friendly representation of binary search node."""

#         return "<binaryNode {}".format(self.data)


####################### Binary Search Tree Find ###################################

class BinarySearchNode(object):
    
    def __init__(self, data, left=None, right=None):
        self.data = data

        self.left = left
        self.right = right


    def find(self, sought):
        """Return node with this data.

        Start here. Return None if not found.
        """

        current = self

        while current:
            print "checking {}".format(current.data)

            if current.data = sought:
                return current
            elif sought < current.data:
                current = current.left
            elif sought > current.data:
                current = current.right

####################### Some trees point up ###################################

class ReverseNode(object):
    """Node that points to its parent"""

    def __init__(self, parent):
        self.parent = parent


####################### Some trees point both ways ###################################

class BidirectionalNode(object):
    """Node that is bidirectional"""

    def __init__(self, parent, children):
        self.parent = parent
        self.children = children
