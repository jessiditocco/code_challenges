######## A Dictionary That Keeps Track of the Order Keys were Added ############

animals = {"duck": 14, "pony": 12, "sheep": 3}

animals["porcupine"] = 7
animals["duck"] = 19

# This wont return the keys in order... it will return it in a random order
print animals.keys() 



################################ Ordered Dict ##################################

class OrderedDict(object):
    """Orderd dictionary, built using a dictionary and a list"""

    def __init__(self):
        self.dict = {}
        self.list = []


    def get(self, key):
        """Get a key O(1)"""

        return self.dict[key]

    def set(self, key, value):
        """Sets a key value pair in the dictionary O(1)"""

        # We want to keep an ordered list of the keys
     
        if key not in self.dict:
            self.dict[key] = value
            self.list.append(key)


    def delete(set, key):
        """Deletes a key in the dictionary"""

        del self.dict[key]

        self.list.remove(key) # O(n)