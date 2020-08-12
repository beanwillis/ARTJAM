from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify
from flask_cors import CORS

from datetime import datetime
from dateutil import tz
import random
import requests
import json
import pika
import uuid
import sys
from os import environ

# Creating the flask application
app = Flask(__name__)

# db settings
# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://admin:jyZhA8uVKSU3rKNv9JhZ@artjam-db.ca7jlm5dqrku.ap-southeast-1.rds.amazonaws.com/artjam-db"

# Binds the database with this specific Flask application
db = SQLAlchemy(app)

# Allow Cross-Origin Resource Sharing making AJAX response possible (Accessing microservice via browser using WAMP/MAMP will cause CORS interimPersona)
CORS(app)


class Books(db.Model):
    """
    A class used to represent the FinalPersona database

    Attributes
    ----------


    Methods
    -------
    json(self)
        Returns a JSON object that represents a row within the database 
    """

    __tablename__ = 'books'

    title = db.Column(db.String(50), nullable=False, primary_key = True)
    author = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    link = db.Column(db.String(300), nullable=False)

    def __init__(self, title, author, description, link):
        """
        Parameters
        ----------

        """
        self.title = title
        self.author = author
        self.description = description
        self.link = link

    def json(self):
        """
        Returns itself as a JSON object 

        Parameters
        ----------
        self
            An instance of itself to convert into json

        """

        return {
            'title' : self.title,
            'author' : self.author,
            'description' : self.description,
            'link' : self.link
        }


@app.route("/get_all_books")
def get_all_book():
    try:
        return {
            'books': [
                books.json() for books in Books.query.all()
            ]
        }, 200
    except Exception as e:
        print(e)
        return {"error": "Cannot retrieve books"}, 500

@app.route("/add_book", methods=["POST"])
def add_book():
    try:
        book_obj = request.get_json()
        title = book_obj["title"]
        author = book_obj["author"]
        description = book_obj["description"]
        link = book_obj["link"]

        new_book = Books(title, author, description, link)
        db.session.add(new_book)
        db.session.commit()
        
        return jsonify({"message" : "book successfully created"}), 201
    except Exception as e:
        print(e)
        return {"error": "Cannot retrieve books"}, 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5003, debug=True)
