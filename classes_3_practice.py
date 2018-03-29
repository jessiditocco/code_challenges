# class Animal(object):
#     hunger = 50 

#     def __init__(self, name):
#         self.name = name


#     def feed(self):
#         self.hunger = self.hunger - 50



# class Cat(Animal):
#     hunger = 20

#     def speak(self):
#         return "Meow, I'm {} the cat".formmat(self.name)


# class Dog(Animal):

#     def speak(self):
#         return "Woof, I'm {} the dog".format(self.name)


#################### We can Refactor to ####################

# class Animal(object):

#     def __init__(self, name, species):
#         self.name = name
#         self.species = species


#     def speak(self, greet="hey"):
#         print "{greet} I'm {name} the {species}".format(greet=self.greet, name=self.name
#             species=self.species)


# class Cat(Animal):

#     def __init__(self, name):
#         return super(Cat, self).__init__(name, "cat")


#     def speak(self):
#         return super(Cat, self).speak("Meow")


# class Dog(Animal):

#     def __init__(self, name):
#         return super(Dog, self).__init__(name, "dog")


#     def speak(self):
#         return super(Dog, self).speak(name, "Woof")



###########We can also factor speak out and set it to class Attribute############

# class Animal(object):

#     greet = "hey"

#     def __init__(self, name, species):
#         self.name = name
#         self.species = species


#     def speak(self):
#         print "{greet} I'm {name} the {species}".format(greet=self.greet, 
#             name=self.name, species=self.species)


# class Cat(Animal):

#     greet = "Meow"

#     def __init__(self, name):
#         return super(Cat, self).__init__(name, "cat")


# class Dog(Animal):

#     greet = "woof"

#     def __init__(self, name):
#         return super(Dog, self).__init__(name, "dog")


########### Examples of Abstract Classes ############

# class AbstractAnimal(object):

#     def __init__(self, name):
#         self.name = name


#     def speak(self):
#         print "{greet} im {name} the {sp}".format(greet=self.greet, name=self.name,
#             sp=self.species)


# class Cat(AbstractAnimal):
#     greet = "meow"
#     species = "cat"


# class Dog(AbstractAnimal):
#     greet = "woof"
#     species = "dog"

# # Notice how Abstract Animal has a speak method which relies on the presence of instance
# # Attributes, not on AbstractANimal
# # This abstract class speak() wont work by itself, but it will work on the subclasses
# # Python has some libraries that make it easy to create abstract classes that are even smarter
# # THey can tell you which methods you need to override or create, and can refuse to make
# # instances of them directly




########### Examples of Mixins ############

class ChaseLaserPointerMixin(object):
    """Can chase laser pointers"""

    def chase_laser(self):
        print "Wee! Im chasing a laser"

class CoverYouInFurMixin(object):
    """Def can cover you in fur"""

    def enfur(self):
        print "(FUR, FUR, FUR)"

# We can subclass from multiple parent classes to use these

class Cat(ChaseLaserPointerMixin, CoverYouInFurMixin, Animal):
    """A Cat"""

    pass

class HairlessRobot(ChaseLaserPointerMixin, Animal):
    """A robot"""

    pass

class Dog(CoverYouInFurMixin, Animal):
    """A dog"""

    pass



