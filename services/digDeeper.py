from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify
from flask_cors import CORS

from datetime import datetime
from dateutil import tz
import random
import requests
import json

import uuid
import sys
from os import environ

# Creating the flask application 
app = Flask(__name__)

# db settings
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://admin:jyZhA8uVKSU3rKNv9JhZ@artjam-db.ca7jlm5dqrku.ap-southeast-1.rds.amazonaws.com/artjam-db"

# Binds the database with this specific Flask application
db = SQLAlchemy(app)

# Allow Cross-Origin Resource Sharing making AJAX response possible (Accessing microservice via browser using WAMP/MAMP will cause CORS issues)
CORS(app)

class DigDeeperDesc(db.Model):
    __tablename__ = 'digdeeperDesc'

    iLikeTo = db.Column(db.String(250), nullable=False, primary_key=True)
    shortDesc = db.Column(db.String(250), nullable=False)
    longDesc = db.Column(db.String(250), nullable=False)


    def __init__(self, iLikeTo, shortDesc, longDesc):

        self.iLikeTo = iLikeTo
        self.shortDesc = shortDesc
        self.longDesc = longDesc

    def json(self):

        return {
            "iLikeTo" : self.iLikeTo,
            "shortDesc" : self.shortDesc,
            "longDesc" : self.longDesc,
        }

@app.route("/get_all")
def get_all():
    return jsonify({"data": [iliketo.json() for iliketo in DigDeeperDesc.query.all()]})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5003, debug=True)