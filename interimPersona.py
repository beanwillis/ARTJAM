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

# Allow Cross-Origin Resource Sharing making AJAX response possible (Accessing microservice via browser using WAMP/MAMP will cause CORS issues)
CORS(app)

class InterimPersona(db.Model):
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

    issues = db.Column(db.String(250), nullable=False, primary_key=True)
    skills = db.Column(db.String(250), nullable=False, primary_key=True)
    interests = db.Column(db.String(250), nullable=False, primary_key=True)
    activities = db.Column(db.String(250), nullable=False)
    schoolActivities = db.Column(db.String(250), nullable=False)
    persona = db.Column(db.String(250), nullable=False)

    def __init__(self, issues, skills, interests, activities, schoolActivities, persona):
        """
        Parameters
        ----------
 
        """
        self.issues = issues
        self.skills = skills
        self.interests = interests
        self.activities = activities
        self.schoolActivities = schoolActivities
        self.persona = persona

    def json(self):
        """
        Returns itself as a JSON object 

        Parameters
        ----------
        self (Appointment object)
            An instance of itself to convert into json

        """

        return {
            "issues" : self.issues,
            "skills" : self.skills,
            "interests" : self.interests,
            "activities" : self.activities,
            "schoolActivities" : self.schoolActivities,
            "persona" : self.persona
        }

@app.route("/get_all_interim_personas")
def get_all_interim_personas():
    try:
        return {
            'interim personas': [
                persona.json() for persona in InterimPersona.query.all()
            ]
        }, 200
    except Exception as e:
        print(e)
        return {"error" : "Cannot retrieve interim personas"}, 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)