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


########## Relationships #####################

class Department(db.Model):
    """Department. A Department has many employees"""

    __tablename__ = "departments"

    dept_code = db.Column(db.String(5), primary_key=True)
    dept_name = db.Column(db.String(20), nullable=True, unique=True)
    phone = db.Column(db.String(20))

    def __repr__(self):
        return "<Department code={} Department name= {}".format(self.dept_code, self.dept_name)

class Employee(db.Model):
    """Employee class"""

    __tablename__ = "employees"

    emp_id = db.Column(db.Integer, autoincrement=True)
    emp_name = db.Column(db.String(30), nullable=True, unique=True)
    dept_code = db.Column(db.String(5), db.ForeignKey('departments.dept_code'))


class Employee(db.Model):
    """Employee class"""

    __tablename__ = "employees"

    emp_id = db.Column(db.Integer, autoincrement=True)
    emp_name = db.Column(db.String(30), nullable=True, unique=True)
    dept_code = db.Column(db.String(5), db.ForeignKey('departments.dept_code'))


    # dept = db.relationship('Department')
    dept = db.relationship('Department', backref='employees')

class Department(db.Model):
    """Department class"""

    __tablename__ = "departments"

    # ...

    employees = db.relationship("Employee")
          

############################### Using Relationships ###############################

def phone_directory_nav():
    emps = Employee.query.all()

    for emp in emps:
        if emp.dept is not None:
            print emp.name, emp.dept.dept_code, emp.dept.phone

# inefficient becuase SQL alchemy fires off several queues
# one for the list of employees
# one for each department

def phone_dir_nav_eager():
    emps = Employee.query.options(db.joinedload('dept')).all()

    for emp in emps:
        if emp.dept is not None:
            print emp.name, emp.dept.dept_code, emp.dept.phone
        else:
            print emp.name, "_", "_"

def phone_dir_join_class():
    emps = db.session.query(Employee.name, Department.dept_name, 
        Department.phone).join(Department).all()

    for name, dept_name, phone in emps:   # [(n, d, p), (n, d, p)]
        print name, dept_name, phone


def phone_dir_join_class():
    emps = db.session.query(Employee, Department).join(Department).all()

    for emp, dept in emps:  # [(<Emp>, <Dept>), (<Emp>, <Dept>)]
        print emp.name, dept.dept_name, dept.phone

def phone_dir_join_outerjoin():
    emps = db.session.query(Employee, Department).outerjoin(Department).all()

    for emp, dept in emps:
        if dept is not None:
            print emp.name, dept.dept_name, dept.phone
        else:
            print emp.name, "-", "-"