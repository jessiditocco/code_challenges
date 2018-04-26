##### Psuedocode ###########

# output could be a dictionary with the keys being the name of the person who owes money
# the value could be a list of tuples (name, money_owed)

# dict = {"jessi": [("john", 25), ("jane", 25), ("joe", 25)],
            # "parul": }
# that way, you could have everybody that owes

# input: could be a list of tuples or lists of lists 
# [(0-- person who paid, 1-- total amount person paid, 2-- [List of Names: name1, name2, name3]), 
# name owes this much money to

def calculate_transactions(lst):
    """
    >>> calculate_transactions(["Jessi", 100, ["John", "Joe", "Jane"]]
    John owes Jessi $25
    Joe owes Jessi $25
    Jane owes Jessi $25
    """

    person_who_paid = lst[0]
    total_amount_paid = lst[1]
    benefactors = lst[2]

    divide_by = len(lst[2]) + 1

    amount_owed = total_amount_paid / divide_by

    for person in benefactors:
        print "{} owes {} ${}".format(person, person_who_paid, amount_owed)


# calculate_transactions(["Jessi", 100, ["John", "Joe", "Jane"]])


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All tests passed!"