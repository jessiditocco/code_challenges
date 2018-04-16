def quicksort(lst):
    """quicksort and return a result."""

    # if the length of the list is less than 2, return the list
    if len(lst) < 2:
        return lst

    # index at half of the list
    mid = int(len(lst) / 2) 
    # select the pivot element
    pivot = lst[mid]

    # partition elements into lo, hi, equal buckets
    lo, hi, eq = [], [], []

    for elem in lst:
        if elem < pivot:
            lo.append(elem)

        elif elem == pivot:
            eq.append(elem)
        # If the element is less than the pivot
        else:
            hi.append(elem)

    # concatenate the sorted buckets and finish
    return quicksort(lo) + eq + quicksort(hi)


    # This implementaiton is still O(n log n), but we are using additional memory
    # For the buckets. During every round, it must place every element into a buckets
    # Concatenating sorted buckets at the end of every round costs
    # and additional O(n)
