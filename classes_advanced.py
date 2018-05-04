##################### Static Methods ##########################

class Cat(object):
    """Our cat class"""


    @staticmethod
    def kibble_to_calories(kibble):
        """Converts one piece of kibble to calories."""

        return kibble * 0.345


###########################  Database Cat ################################

CAT_UPDATE = "UPDATE Cats SET hunger = :hunger WHERE name = :name"

class Cat2(object):
    # ..

    def feed(self, calories):
        """Feed cat, update hunger, and update database."""

        self.hunger = self.hunger - calories
        db.session.execute(CAT_UPDATE, {"hunger": self.hunger, "name": self.name})
        db.session.commit()


CAT_SELECT = "SELECT name, hunger FROM Cats WHERE name = :name"

def get_cat_from_db(name):
    """Get cat with given name from database"""

    cursor = db.session.execute(CAT_SELECT, {"name": name})
    cat_db_row = cursor.fetchone()
    hunger = cat_db_row[1] # row is (name, hunger)

    return Cat2(name, hunger)

###########################  Keep Things in the Class ################################

class Cat3(object):
    """Cat with class methods"""

    _SELECT = "SELECT name, hunger FROM Cats WHERE name = :name"
    _UPDATE = "UPDATE Cats SET hunger = :hunger WHERE name = :name"

    def __init__(self, name, hunger): # specialmethod
        self.name = name
        self.hunger = hunger


    def feed(self, calories):
        """Feed cat, update hunger, and update database"""

        self.hunger = self.hunger - calories

        db.session.exectue(self._UPDATE, {"hunger": self.hunger, "name": self.name})
        db.session.commit()

###########################  Class Method ################################

class Cat5(object):

    _SELECT = "SELECT name, hunger FROM Cats WHERE name = :name"
    _UPDATE = "UPDATE Cats SET hunger = :hunger WHERE name = :name"

    # ...

    @classmethod
    def get_cat_from_db(cls, name):
        """Get cat with given name from database."""

        cursor = db.session.execute(cls._SELECT, {"name": name})
        cat_row = cursor.fetchone()

        hunger = cat_db_row[1]

        return cls(name, hunger)


###########################  Class Method and Inheritance ################################

class Animal(object):

    @staticmethod
    def make_one():
        """Make an instance."""

        return Animal()

class Cat(Animal):
    """Cat"""

class Animal(object):

    @classmethod
    def make_one(cls):
        return cls()

class Cat(Animal):
    """Cat"""
