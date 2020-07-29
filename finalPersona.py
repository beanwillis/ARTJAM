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
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://admin:jyZhA8uVKSU3rKNv9JhZ@artjam-db.ca7jlm5dqrku.ap-southeast-1.rds.amazonaws.com/artjam-db"

# Binds the database with this specific Flask application
db = SQLAlchemy(app)

# Allow Cross-Origin Resource Sharing making AJAX response possible (Accessing microservice via browser using WAMP/MAMP will cause CORS interimPersona)
CORS(app)


class FinalPersona(db.Model):
    """
    A class used to represent the InterimPersona database

    Attributes
    ----------


    Methods
    -------
    json(self)
        Returns a JSON object that represents a row within the database 
    """

    __tablename__ = 'interimpersona'

    interimPersona = db.Column(db.String(250), nullable=False, primary_key=True)
    likeTo = db.Column(db.String(250), nullable=False, primary_key=True)
    finalPersona = db.Column(db.String(250), nullable=False, primary_key=True)
    description = db.Column(db.String(500), nullable=False)
    quotes = db.Column(db.String(500), nullable=False)
    skills = db.Column(db.String(500), nullable=False)
    books = db.Column(db.String(250), nullable=False)

    def __init__(self, interimPersona, likeTo, finalPersona, description, quotes, persona):
        """
        Parameters
        ----------

        """
        self.interimPersona = interimPersona
        self.likeTo = likeTo
        self.finalPersona = finalPersona
        self.description = description
        self.quotes = quotes
        self.skills = persona
        self.books = books

    def json(self):
        """
        Returns itself as a JSON object 

        Parameters
        ----------
        self (Appointment object)
            An instance of itself to convert into json

        """

        return {
            "interimPersona": self.interimPersona,
            "likeTo": self.likeTo,
            "finalPersona": self.finalPersona,
            "description": self.description,
            "quotes": self.quotes,
            "skills": self.skills,
            "books": self.books
        }


@app.route("/get_all_final_personas")
def get_all_final_personas():
    try:
        return {
            'final personas': [
                persona.json() for persona in FinalPersona.query.all()
            ]
        }, 200
    except Exception as e:
        print(e)
        return {"error": "Cannot retrieve final personas"}, 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
