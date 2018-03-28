import random 

class Animal(object):
    """An animal class"""

    name = None
    species = "dog"

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.age = random.randint(1, 10)


    def speak(self):
        return "Woof! I am a {species} named {name}".format(species=self.species, 
            name=self.name)


    def graduate(self):
        self.name = "Dr " + self.name


    def do_trick(self):
        print "(Wags tail)"
        print self.speak()




fido = Animal("Fido", "dog")

print fido.speak()

print fido.name


class MyClass(object):
    """Class attributes vs. instance attributes"""

    class_attr = 1

    def __init__(self):
        self.instance_attr = 1

# Lets make an instance of my class

o = MyClass()

print o.class_attr  # should be 1
print o.instance_attr   # should be 1

MyClass.class_attr = 2 
print o.class_attr  # should be 2

o.class_attr = 3
print o.class_attr  # should be 3

MyClass.class_attr = 4

print o.class_attr  # should be 3
