def lazy_lemmings(num_holes, cafes):
    """
    >>> lazy_lemmings(6, [2, 4])
    2

    """

    # Loop through each hole in the range of num holes
    # For each hole, subtract the cafes from that hole and create a list of these numbers
    # Take the minimum of this list
    # Check to see whether this minimum is greater than the worst and if so, update it
    # Return the worst distance

    longest_distance = 0

    for hole in range(num_holes):
        distance = min([abs(hole - cafe) for cafe in cafes])

        # if distance > longest_distance:
        #     longest_distance = distance

        longest_distance = max(longest_distance, distance)


    return longest_distance


    # The runtime for this solution is O(n^2) because we are scanning each cafe for each hole

    # A better solution would let us find the nearest hole for a cafe quickly. We can use binary search?
    


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All tests passed!"



