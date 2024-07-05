from flask import Flask
from flask_sqlalchemy import SQLAlchemy

"""This code sets up a SQLAlchemy Flask web application"""

app = Flask(_name_)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

