# IGNORE THIS FOR NOW
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__, template_folder='../frontEnd/templates')

# Database stuff created by following https://www.youtube.com/watch?v=cYWiDiIUxQc
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)


class User(db.Model):  # With SQLAlchemy, tables are represented as classes, which makes more sense
    id = db.Column(db.Integer, primary_key=True)  # unique id for the user
    # max of 20 characters, has to be unique, can't be null
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    # one to many relationship, ie. one user can have many posts
    # backref is like creating another column
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):  # describes how the object is printed whenever we print it out
        return f"User('{self.username}', '{self.email}', '{self.username}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user.id'), nullable=False)  # each post has a used id

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}', '{self.date_posted}'"
