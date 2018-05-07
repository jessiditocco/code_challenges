class Cat(db.Model):
    """Feline cat"""

    __tablename__ = "cats"

    cat_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    color = db.Column(db.String(50))
    hunger = db.Column(db.Integer, nullable=False)


    def greet(self):
        """Greet using name"""

        return "I am {}".format(self.name)

    def feed(self, units=10):
        """Nom, nom nom"""

        self.hunger -= units
        self.hunger = max(self.hunger, 0)

    def __repr__(self):
        """Useful representation"""

        return "<Cat{} Name{}".format(self.id, self.name)


########## Queries #####################

Cat.query.all()

# SELECT * FROM cats;

Cat.query.get(1)

# SELECT * FROM catas WHERE cat_id = 1

Cat.query.filter_by(color="grey").all()

# SELECT * FROM cats WHERE color='grey'

Cat.query.filter(Cat.color == 'grey').all()

# SELECT * FROM cats WHERE color='grey'

Cat.query.filter(Cat.hunger < 10, Cat.color == 'grey').all()

# SELECT * FROM cats WHERE hunger < 10 AND color = 'grey'


########## Class Methods #####################

class Cat(db.Model):
    __tablename__  = "cats"

    @classmethod
    def get_by_color(cls, color):
        """Gets all cats matching that color"""

        return cls.query.filter_by(color=color).all()

########## SETUP #####################
db = SQLAlchemy()


def connect_to_db(app):
    """Connect to database"""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cats'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)



connect_to_db(app)




########## Flask-SQL Alchemy #####################

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

DB_URI = "postgresql:///cats"

# everything comes off this tidy object

db = SQLAlchemy()


class Cat(db.Model):
    name = db.Column(db.String(50))

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
db.app = app
db.init_app(app)

db.create_all()

# add cats

auden = Cat(name="auden")
db.session.add(auden)
db.session.commit()