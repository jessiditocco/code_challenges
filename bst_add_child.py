class Node(object):

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.right = right
        self.left = left

    def __repr__(self):
        return "<Node {}>".format(self.data)


    def insert(self, new_data):
        """Insert new node with `new_data` to BST tree rooted here."""

        # check the new_data against the current data
            # if the new data is bigger, go right
            # if new data is smaller, go left

        current = self.data

        while current.left or current.right is not None:
            if new_data > current.data:
                current = self.right
            elif new_data < current.data:
                current = self.left





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

if __name__ == "__main__":
    t = Node(4, 
        Node(2, Node(1), Node(3)),
        Node(7, Node(5), Node(8))
        )
    insert(self, 0)

    if t.left.left.left == 0:
        print "Passed!"
    
