# Do two numbers in a list sum to zero?

def sum_to_zero(lst):
    """Checks to see if two numbers in a list sum to zero."""

    nums = set(lst)

    for num in lst:
        if (-num) in nums:
            return True

    return False