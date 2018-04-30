import csv
import sys

def get_customer_pages_by_id(customer_id):

    pages_customer_viewed = []

    with open(sys.argv[1]) as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        for row in reader:
            if row[1].strip(",") == customer_id:
                pages_customer_viewed.append(row[2])

    print pages_customer_viewed
    return pages_customer_viewed

get_customer_pages_by_id(sys.argv[2])