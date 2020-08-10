from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
import json

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://flight_admin:6kKVm7C2PHtVtgGT@esd-g7t6-rds.cs2kfkrucphj.ap-southeast-1.rds.amazonaws.com:3306/flight_name'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://flight_admin:6kKVm7C2PHtVtgGT@esd-g7t6.cakxlnvku8py.ap-southeast-1.rds.amazonaws.com:3306/flight_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 10,'pool_recycle': 1800}

db = SQLAlchemy(app)
CORS(app)


class Flight(db.Model):
    __tablename__ = 'flight'

    flightNo = db.Column(db.String(8), primary_key=True)
    departDest = db.Column(db.String(5), nullable=False)
    arrivalDest = db.Column(db.String(5), nullable=False)
    deptTime = db.Column(db.DateTime, nullable=False)
    arrivalTime = db.Column(db.DateTime, nullable=False)
    basePrice = db.Column(db.String(30), nullable=False)
    # type = db.Column(db.String(1), nullable=False)

    def __init__(self, flightNo, departDest, arrivalDest, deptTime, arrivalTime, basePrice):
        self.flightNo = flightNo
        self.departDest = departDest
        self.arrivalDest = arrivalDest
        self.deptTime = deptTime
        self.arrivalTime = arrivalTime
        self.basePrice = basePrice
        # self.type = type

    def json(self):
        return {
            "flightNo": self.flightNo,
            "departDest": self.departDest,
            "arrivalDest": self.arrivalDest,
            "deptTime": str(self.deptTime),
            "arrivalTime": str(self.arrivalTime),
            "basePrice": self.basePrice,
            # "type" : self.type
        }


class Code(db.Model):
    __tablename__ = 'code'

    code = db.Column(db.String(3), primary_key=True)
    name = db.Column(db.String(45))  # , nullable=False

    def __init__(self, code, name):
        self.code = code
        self.name = name

    def json(self):
        return {
            "code": self.code,
            "name": self.name
        }


@app.route("/flight")
def get_all():
    return {"flight": [flight.json() for flight in Flight.query.all()]}
t