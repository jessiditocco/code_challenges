def reverse_list_recursively(lst):
    """Reverses a list using recursion"""


    # basecase will be when the length of the list is less than 2
    # return the list

    # we want to return the last item popped from the list as a new list
    # and we want to add that to the function call reverse_list_recursivley
    # on that new list which will have the last item popped off

    if len(lst) < 2:
        return lst

    return [lst.pop()] + reverse_list_recursively(lst)