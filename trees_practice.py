# class Node(object):
#     """Node in a tree"""

#     # def __init__(self, data, children=None):
#     #     self.data = data
#     #     if not children:
#     #         self.children = []
#     #     else:
#     #         self.children = children

#     # A freindly more idiomatic version of this would be

#     def __init__(self, data, children=None):
#         self.data = data
#         self.children = children or []
#         # Since if children is None, it will move to the next part of the expression
#         # And so children will be[]


#     def __repr__(self):
#         """Reader-friendly representation"""

#         return "<Node {}>".format(self.data)


################### Finding a node: Depth First ################################

# class Node(object):

#     def find(self, data):
#         """Return node object with this data.

#         Start here. Return None if not found.
#         Finding a node using depth first search.
#         """

#         to_visit = [self]

#         while to_visit:
#             current = to_visit.pop()

#             if current.data == data:
#                 return current

#             to_visit.extend(current.children)


################### Finding a node: Breadth First ################################

# class Node(object):

#     def find(self, data):
#         """Finding a node with breadth first search

#         Returns the Highest-Ranking
#         """

#         to_visit = []

#         while to_visit:
#             current = to_visit.pop(0)

#             if current.data == data:
#                 return current

#             to_visit.extend(current.children)

################### Tree Class ################################

# class Node(object):
    
#     def __init__(self, data, children=None):
#         self.data = data

#         self.children = children or []    


# class Tree(object):
#     """A tree class."""

#     def __init__(self, root):
#         self.root = root


# class School(object):
#     """A school represented as a tree"""

#     def __init__(self, headmaster):
#         self.headmaster = headmaster


################### Find in Tree ################################

class Tree(object):
    def find_in_tree(self, data):
        """Return node object with this data.

        Start at root. Return none if not found.
        """

        return self.root.find(data)


class Node(object):
    def find(self, data):
        """Return Node object with this data.

        Start here. Return none if not found
        """

        to_visit = [self]

        while to_visit:
            current = to_visit.pop()

            if current.data == data:
                return current

            to_visit.extend(current.children)
