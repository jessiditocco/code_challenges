"""Using a queue to make a console to make a console task manager"""

class Queue(object):
    """A simple queue, implemented using a list."""

    # NOTE: this is a straightforward way to implement a
    # queue -- but it's also inefficient if you'll have
    # many items in the queue. For a more efficient queue
    # implementation, you could build a Queue class
    # yourself using a doubly-linked list, or you could use
    # the Queue class included in Python's standard library,
    # "collections.deque" ("deque" = "double-ended queue")
    
    def __init__(self):
        self._data = []

    def enqueue(self, item):
        """Add an item to the end of the list"""

        self._data.append(item)

    def dequeue(self):
        """Remove an item from the front of the queue"""

        return self._data.pop(0)

    def peak(self):
        """Show the first item in the queue"""

        return self._data[0]

    def is_empty(self):
        """Is the queue empty?"""

        # If the queue is an empty list, self._data would return False
        # So if the queue is empty we want to return true
        # modify with not self._data
        return not self._data


# Instantiate our task_queue

task_queue = Queue()

while True:
    # we want to display to the user the next task to be done
    # we want to ask the user for input to add a task, do the task, or quit

    if task_queue.is_empty():
        next_task = None
    else:
        next_task = task_queue.peak()

    print "Next task:", next_task

    command = raw_input("A)dd task, D)o first task, or Q)uit? ")

    if command == "A":
        new_task = raw_input("Okay, what is your new task? ")
        task_queue.enqueue(new_task)

    elif command == "D":
        print "Okay, finished", task_queue.dequeue()

    elif command == "Q":
        break

    else:
        print "That is an invalid command; try again"
