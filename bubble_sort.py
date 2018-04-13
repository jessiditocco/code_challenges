################################  Bubbling Up #################################

def bubble_up(lst):
    """Bubble the highest number to the end"""

    # loop through every number in the length of the list - 1
    # for each of these numbers though, we have to check it against every
    # number in the list so we have to have two nested for loops


    for i in range(len(lst) - 1):

        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                lst[j + 1], lst[j] = lst[j], lst[j + 1]

################################  Optimizing #################################

def shorter_bubble_sort(lst):
    """Shorter bubble sort"""

    for i in range(len(lst) - 1):
        # don't re-check already-sorted
        # We will subtract i to reduce the number of spots that the
        # inner loop has to go
        for j in range(len(L) - 1 - i): 
            if lst[j] > lst[j + 1]:
                # Pair out-of-order, swap them
                lst[j + 1], lst[j] = lst[j], lst[j + 1]



################ Stopping bubble Sort Once list is Sorted ########################

def best_bubble_sort(lst):
    """Shorter and fast-win bubble sort"""

    for i in range(len(lst) - 1):
        # keep track of whether we made a swap

        made_swap = False
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                made_swap = True

            if not made_swap:
                # if no swap was made, the list is already Sorted
                break

