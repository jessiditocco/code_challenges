class Queue(object):
    """A class for a queue, implemented using a list"""

    def __init__(self):
        self.data = []


    def enqueue(self, item):
        """Appends an item to the top of a queue"""

        self.data.append(item)


    def dequeue(self):
        """Removes an item from the qudataeue and returns that item"""

        return self.data.pop(0)


    def peak(self):
        """Shows the next item in the queue"""

        return self.data[0]


    def is_empty(self):
        """Returns boolean denoting if the queue is empty."""

        return not self.data


task_queue = Queue()

# while true
# we will check if the queue is empty; if it is... the next task is None
# if it is not empty, we will return to the user the next task
# If next task is not none, we will ask the user if they would like to add a task, perform a task, or exit
# If the next task is none, we will ask the user if they would like to add a task or exit

while True:

    if task_queue.is_empty():
        next_task = "You currently have no tasks in the queue"
        print "Would you like to add a task?"
        
        command = raw_input("Y or N? ")

        if command == "Y":
            task = raw_input("What task would you like to add? ")
            task_queue.enqueue(task)
        elif command == "N":
            print "Okay, see you next time"
            break
        else:
            print "Invalid command"
    else:
        next_task = task_queue.peak()
        print "Your next task is {}".format(next_task)
        print "Would you like to A) Add a task B) Complete a task C) Exit out of the task manager"
        
        command = raw_input("> ").capitalize()
        print command

        if command == "A":
            print "What task would you like to add?"
            task = raw_input("> ")
            task_queue.enqueue(task)

        elif command == "B":
            print "Completing {}".format(task_queue.dequeue())

        elif command == "C":
            break
        else:
            print "Invalid option. Please Try again"



