
############################## Linked List Basics    ########################

# class Node(object):
#     """Node in a linked list"""

#     def __init__(self, data):
#         self.data = data
#         self.next = None


# apple_node = Node("apple")
# berry_node = Node("berry")
# cherry_node = Node("cherry")

# apple_node.next = berry_node
# berry_node.next = cherry_node


# class LinkedList(object):
#     """LinkedList"""

#     def __init__(self):
#         self.head = None
#         # We can add a tail so that appending will be O(1)
#         self.head = None



############################## Traversing a linked list ########################

class LinkedList(object):
    # Traversing the list. Lets assume we have already built the list
    # We want to traverse the list and print it

    def print_list(self):
        """Print all of the items in the list"""

        current = self.head

        while current is not None:
            print current.data
            curent = current.next

    # Checking to see if data exists in our linked list

    def find(self, data):
        """Does this data exist in our list?"""

        current = self.head

        while current is not None:
            if current.data == data:
                return True
            current = current.next

        return False

    def append(self, data):
        """Append node with data to the end of the list."""

        # Create a new node with passed in data
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        if self.head is not None:
            # Did the list start as empty?
            self.tail.next = new_node

        self.tail = new_node