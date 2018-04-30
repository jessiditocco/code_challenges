from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension


db = SQLAlchemy()

app = Flask(__name__)
app.secret_key = "SECRET!"


@app.route("/")
def index():
    """Execute queries in the Melon DB when loading the homepage"""

    cursor = db.session.execute("SELECT name, price FROM melons")
    one_melon = cursor.fetchone()
    two_melons = cursor.fetchmany(2)
    all_melons = cursor.fetchall()

    print one_melon
    print two_melons
    print all_melons

    db.session.execute(
        """INSERT INTO melons (name, type, price)
        VALUES ('Jess', 'watermelon', 100.00)""")

    db.session.commit()

    return render_template("homepage.html", one_melon=one_melon, two_melons=two_melons, all_melons=all_melons)


##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect to database."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///melondb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    connect_to_db(app)
    app.debug = True
    DebugToolbarExtension(app)
    app.run(host="0.0.0.0")