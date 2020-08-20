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

    iLikeTo = db.Column(db.String(200), nullable=False, primary_key=True)
    shortDesc = db.Column(db.String(100), nullable=False)
    longDesc = db.Column(db.String(500), nullable=False)


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

@app.route("/get_iLikeTo")
def get_iLikeTo():
    try:
        query = db.session.query(DigDeeperDesc.iLikeTo.distinct())
        
        return {
            'iLikeTo': [
                DigDeeperDesc[0] for DigDeeperDesc in query.all()
            ]
        }, 200
    except Exception as e:
        print(e)
        return {"error" : "Cannot retrieve iLikeTO"}, 500
        
@app.route("/get_dig_deeper_desc/<string:iLikeTo>")
def get_desc_by_ilt(iLikeTo):
    desc = DigDeeperDesc.query.filter_by(iLikeTo=iLikeTo).first()
    if desc:
        return {"data": desc.json(), "status": 200}
    return jsonify({"message": "iLikeTo not found"}), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5003, debug=True)