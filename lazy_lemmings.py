def lazy_lemmings(num_holes, cafes):
    """
    >>> lazy_lemmings(6, [2, 4])
    2

    """


    # Loop through each hole in the range of num holes
    # For each hole, subtract the cafes from that hole and create a list of these numbers
    # Take the minimum of this list
    # Check to see whether this minimum is greater than the worst and if so, update it
    # # Return the worst distance

    longest_distance = 0

    for hole in range(num_holes):
        distance = min([abs(hole - cafe) for cafe in cafes])

        # if distance > longest_distance:
        #     longest_distance = distance

        longest_distance = max(longest_distance, distance)


    return longest_distance


    # The runtime for this solution is O(n^2) because we are scanning each cafe for each hole

def lazy_lemmings_optimized(num_holes, cafes):
    """
    Find the longest distance between a hole and a cafe.
    This solution uses binary search to quickly find the one or two
    cafes closes to the hole. This makes the problem O(n log n) rather
    than O n^2.

    >>> lazy_lemmings(6, [2, 4])
    2

    """


    from bisect import bisect_left


    # A better solution would let us find the nearest hole for a cafe quickly. We can use binary search?
    # Think about ways you could improve this... Is there a way to search a list 
    # For a value quickly?
    # A better solution would be to let us find the nearest hole for a cafe quickly
    # We can use binary search for this:

    # in this approach, we will use binary search to find the location
    # python uses bisect module (array bisection algorithm)

    # We have four cases to consider:
        # This hole is after all cafes, so find the distance to the last cafe
        # This hole is before all cafes, so find the distance to the first cafe
        # This hole is a cafe, so the distance is zero
        # This hole is between two cafes, so find the smallest travel distance between them 

    worst = 0

    for hole in range(num_holes):
        # Find the place we would insert this hole into the sorted cafes list

        idx = bisect_left(cafes, hole)

        if idx == len(cafes):
            # This hole is after all of the cafes so the distance is from this
            # hole to the cafe before it

            dist = hole - cafes[idx - 1]

        elif idx == 0:
            # This hole is before all the cafes, so the distance
            # is from this hole to the cafe after it

            dist = cafe[idx] - hole

        elif cafes[idx] == hole:
            # This hole is a cafe, so no travel is needed!
            dist = 0

        else:
            # This hole is between two cafes, so use the smaller
            # Distance between them

            dist = min(hole - cafes[inx - 1], cafes[indx] - hole)

        # Keep track of the longest distance we have seen
        worst = max(worst, dist)



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All tests passed!"



