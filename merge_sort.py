############################# Merge Sort #######################################

def make_one_sorted_list(lst1, lst2):
    """Merge two sorted lists"""

    merged_list = []

    while len(lst1) > 0 or len(lst2) > 0:
        if lst1 == []:
            merged_list.extend(lst2)
        elif lst2 == []:
            merged_list.extend(lst1)
        elif lst1[0] < lst2[0]:
            merged_list.append(lst1.pop(0))
        else:
            merged_list.append(lst2.pop(0))

    return merged_list


############################# Make Everything a List of One #######################################

def make_everything_a_list_of_one(lst):
    """Divide lists until we reach lists of length 1."""

    # if the length of the list is 1, return the list
    # find the index of the midpoint of the list
    # divide the list in half and assign the other half

    if len(lst) < 2:
        print lst,
        return lst

    mid = int(len(lst) / 2)

    make_everything_a_list_of_one(lst[:mid])
    make_everything_a_list_of_one(lst[mid:])

########################### Merge Sort ######################################

def merge_sort(lst):
    """Merge sort a list and return the result."""

    # break everything down into a list of one using recursion
    # If the length of the list is 1, return the list
    if len(lst) < 2:
        return lst

    # index at half of the list
    mid = int(len(lst) / 2)

    # divide the list in half
    lst1 = merge_sort(lst[:mid])
    # assign the other half
    lst2 = merge_sort(lst[mid:])

    return make_merge(lst1, lst2)


def make_merge(lst1, lst2): 
    """Merge the two lists"""

    result_list = []
    print lst1, lst2

    while len(lst1) > 0 or len(lst2) > 0:
        if lst1 == []:
            result_list.append(lst2.pop(0))
        elif lst2 == []:
            result_list.append(lst1.pop(0))
        elif lst1[0] < lst2[0]:
            result_list.append(lst1.pop(0))
        else:
            result_list.append(lst2.pop(0))

    print result_list
    return result_list

print merge_sort([2, 1, 7, 4])
