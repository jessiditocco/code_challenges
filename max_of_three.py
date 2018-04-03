def maxofthree(num1, num2, num3):
    """Returns the largest of three integers

    >>> maxofthree(1, 5, 2)
    5

    >>> maxofthree(10, 1, 11)
    11

    """

    # nums = [num1, num2, num3]
    # largest = nums[0]

    # for num in nums:
    #     if num > largest:
    #         largest = num

    # return largest

    # This would be O(n) runtime because we are looping through each number in our list

    if num1 >= num2 and num1 >= num3:
        return num1

    elif num2 >= num1 and num2 >=num3:
        return num2

    elif num3 >= num2 and num3 >= num1:
        return num3

    else:
        return "Something went wrong"




if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All tests passed!"