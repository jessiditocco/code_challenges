def missing_number(lst_nums, max_num):
    """
    >>> missing_number([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)
    8
    """

    # sort the list
    # if list at zero is not equal to 1
    # return 1
    # if the list at -1 index is not max number
    # Return max number
    # use enumerate to loop through the entire length of the list--
    # if the number that we are on is not one less than the next number
    # return that number plus 1


    sorted_nums = sorted(lst_nums)

    if sorted_nums[-1] != max_num:
        return max_num

    for i in range(len(sorted_nums) - 1):
        if sorted_nums[i] != (sorted_nums[i + 1] - 1):
            return sorted_nums[i] + 1

    # The other option is to use expected sum
    # For a clever math formula-- you can sum the numbers
    # and subtract the sum from the expected sum to reaveal the missing numbers

    # expected_sum = sum(range(max_num + 1))

    # return expected_sum - sum(lst_nums)



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All tests passed!!"

