"""Given a triangle of values, find highest-scoring path.

For example::

      2
     5 4
    3 4 7
   1 6 9 6   = [2,4,7,9] = 22

This works:

    >>> triangle = make_triangle([[2], [5, 4], [3, 4, 7], [1, 6, 9, 6]])
    >>> triangle
    [2, 5, 4, 3, 4, 7, 1, 6, 9, 6]
    >>> maxpath(triangle)
    22
"""

class Node(object):
    """Basic node class that keeps track of parents and children.

    This allows for multiple parents-- so this isn't for trees, where
    nodes can only have children. It is for 'directed graphs'.
    """


    def __init__(self, name):
        self.name = name
        self.children = []
        self.parents = []

def make_triangle(self, nodes):
    """Make a triangle given a list of levels.

     For example, imagining this triangle::

               1
              2 3
             4 5 6
            7 8 9 10

    We could create it like this::

        >>> triangle = make_triangle([[1], [2,3], [4,5,6], [7,8,9,10]])
        >>> triangle
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    Let's check to make sure this works::

        >>> n1, n2, n3, n4, n5, n6, n7, n8, n9, n10 = triangle
        >>> n1.parents
        []
        >>> n1.children
        [2, 3]
        >>> n2.parents
        [1]
        >>> n2.children
        [4, 5]
        >>> n3.parents
        [1]
        >>> n3.children
        [5, 6]
        >>> n4.parents
        [2]
        >>> n4.children
        [7, 8]
        >>> n5.parents
        [2, 3]
        >>> n5.children
        [8, 9]
        >>> n6.parents
        [3]
        >>> n6.children
        [9, 10]

    """

    
    nodes = []
    for y, row in enumerate(levels):
        for x, value in enumerate(row):
            node = row[x] = Node(value)
            nodes.append(node)
            if y == 0:
                continue
            if x == 0:
                parents = [levels[y - 1][0]]
            elif x == y:  # last in row
                parents = [levels[y - 1][x - 1]]
            else:
                parents = [levels[y - 1][x - 1],
                           levels[y - 1][x]]
            node.parents = parents
            for p in parents:
                p.children.append(node)
    return nodes


def maxpath(nodes):
    """Given list of nodes in triangle, return high-scoring path."""
    
    # We can do this without having to traverse multipe paths, but just by
    # visiting each node, and looking at it's parent's nodes

    # START SOLUTION
    # best score we have seen so far
    best = 0

    # Loop through each nodes list
    for n in nodes:
        if not n.parents:
            # For the root, it has no best-path
            n.best = n.value
        else:
            # Take the best score of your higher parent and add this value
            n.best = n.vale + max([p.best for p in n.parents])

        # update the best- we've-seen
        best = max(n.best, best)

    return best


if __name__ == '__main__':
    import doctest

    print
    if doctest.testmod().failed == 0:
        print "\t*** ALL TESTS PASSED; GOOD WORK!"
    print