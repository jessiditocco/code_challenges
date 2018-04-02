# def find_largest_smaller_than(nums, xnumber):
#     """Find largest number in sorted list that is smaller than given number.

#     >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 10)
#     2

#     >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 33)
#     4

#     >>> find_largest_smaller_than([-5, -2, 8, 12, 32], -1)
#     1

#     >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 8)
#     2

#     >>> find_largest_smaller_than([-5, -2, 8, 12, 32], -10) is None
#     True

#     """

# # Given an ordered list of numbers and a number, 
# # return the index of the largest number in the list that is 
# # smaller than that number.
    
#     # larg_num_index = 
#     # Loop through each number in the list using enumerate function
#     # If the number that your on is smaller than or equal to itself, return the index
#     # Return none if no numbers are smaller than itself

#     # Fail-fast optimzation: since the list is sorted, if the first number is 
#     # bigger, than we know that a smaller number isn't in our list

#     if nums[0] > xnumber:
#         return None

#     # Optimization: if the last number is smaller than the given number, it must be the asnwer
#     # We need to return the index of the last number

#     if nums[-1] < xnumber:
#         return len(nums) - 1

#     larg_num_index = None

#     # Else, we must loop through the entire list
#     for index, num in enumerate(nums):
#         if num <= xnumber:
#             larg_num_index = index

#     return larg_num_index

# # This solution has O(n) runtime becuase we are looping through the list. There are two cases
# # in which it can get out of the loop fast but it still scales with n

from bisect import bisect_left

def find_largest_smaller_than_bisect(nums, xnumber):
    """
    >>> find_largest_smaller_than_bisect([-5, -2, 8, 12, 32], 10)
    2

    >>> find_largest_smaller_than_bisect([-5, -2, 8, 12, 32], 33)
    4

    >>> find_largest_smaller_than_bisect([-5, -2, 8, 12, 32], -1)
    1

    Never find xnumber --- it's not smaller than itself!

    >>> find_largest_smaller_than_bisect([-5, -2, 8, 12, 32], 8)
    1

    If no such number exists, return None:

    >>> find_largest_smaller_than_bisect([-5, -2, 8, 12, 32], -10) is None
    True
    """

    # O(logn) solution
    # Since we have a list, we can search it quickly using binary search
    # Python has a library, called "bisect" that can do this
    # Python provides the bisect algorithms using the module "bisect" which allows
    # To keep the list in sorted order after insertion of each element
    # This is essential as it reduces the overhead time required to sort the list 
    # again and again after insertion of each element 

    # bisect_left(list, num, beg, end).. this function returns the position in the sorted
    # list where the number passed in the argument can be placed so as to maintain
    # the resultant list in sorted order
    # if the element is already present in the list, the left most position where the element
    # has to be inserted is returned


    # Fail-Optimization: Since our list is sorted, if the first number is bigger
    # a smaller number isn't in our list

    # Since our list is sorted, if the first number is larger than our number, return None


    if nums[0] > xnumber:
        return None
        
    insertion_point = bisect_left(nums, xnumber)

    return insertion_point - 1

    if nums[insertion_point] == xnumber:
        return insertion_point - 1

    else:
        return insertion_point



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "yay passed all tests"