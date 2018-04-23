class Node(object):

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.right = right
        self.left = left

    def __repr__(self):
        return "<Node {}>".format(self.data)


    def insert(self, new_data):
        """Insert new node with `new_data` to BST tree rooted here.
        >>> t.insert(0)

        >>> t.left.left.left.data == 0
        True

        >>> t.left.left.right is None
        True

        >>> t.insert(9)

        >>> t.right.right.right.data == 9
        True

        >>> t.right.right.left is None
        True

        >>> t.insert(6)

        >>> t.right.left.right.data == 6
        True

        >>> t.right.left.left is None
        True
        """

        # # check the new_data against the current data
        #     # if the new data is bigger, go right
        #     # if new data is smaller, go left

        # current = self

        # while current.left is not None or current.right is not None:
        #     if new_data < current.data:
        #         current = current.left
        #     elif new_data > current.data:
        #         current = current.right

        # if new_data < current.data:
        #     current.left = Node(new_data)
        # else:
        #     current.right = Node(new_data)

        # we can also solve this using recursion
        # we should head left or right depending on whether the new
        # data is greater than or less than the node we are on
        # once we go one direction: say we go right, if the current.right
        # is none, we want to add the node there
        # if the current right is not none, we will call the function recursively

        if new_data >= self.data:
            if self.right is None:
                self.right = Node(new_data)
            else:
                self.right.insert(new_data)

        else:
            if self.left is None:
                self.left = Node(new_data)
            else:
                self.left.insert(new_data)



# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# node5 = Node(5)
# node6 = Node(6)
# node7 = Node(7)
# node8 = Node(8)

# node4.right = node7
# node4.left = node2
# node2.right = node3
# node2.left = node1
# node7.right = node8 
# node7.left = node5


t = Node(4, 
    Node(2, Node(1), Node(3)),
    Node(7, Node(5), Node(8))
    )
   
if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All tests passed!!!"
