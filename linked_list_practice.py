
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


class LinkedList(object):
    """LinkedList"""

    def __init__(self):
        self.head = None
        # We can add a tail so that appending will be O(1)
        self.tail = None



############################## Traversing, Searching, Appending, Removing a linked list ########################

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

        if self.tail is not None:
            self.tail.next = new_node
        
        self.tail = new_node



############################## Removing and Item from a Linked List ########################

class LinkedList(object):
    def remove(self, value):
        # If removing the head, you need to point the second item (if any) the new .head
        # If the head is not None and the head's data is equal to the value
        if self.head is not None and self.head.data == value:
            # Set the head equal to the next of the head
            self.head = self.head.next
            # Now, if the head is None (the list is empty now)
            if self.head is None:
                # Set the tail equal to none and return out of the function
                self.tail = None
            return 

        # Removing something other than the head
        # Set the current to the head
        current = self.head
        # Keep traversing until the currents next is None
        while current.next is not None:
            # If the current's next data is equal to the value we are looking for, set the current.next to
            # the currents, next, next
            if current.next.data == value:
                current.next = current.next.next
                # If you're removing the last item and the current.next is None, update the tail
                if current.next is None:
                    # If removing the last item, update .tail
                    self.tail = current
                return 
            # Havent found the value yet, keep traversing 
            else:
                current = current.next
                
