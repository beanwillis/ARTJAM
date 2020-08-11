from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
import json

app = Flask(__name__)

# db settings
# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://admin:jyZhA8uVKSU3rKNv9JhZ@artjam-db.ca7jlm5dqrku.ap-southeast-1.rds.amazonaws.com/artjam-db"

# Binds the database with this specific Flask application
db = SQLAlchemy(app)

# Allow Cross-Origin Resource Sharing making AJAX response possible (Accessing microservice via browser using WAMP/MAMP will cause CORS interimPersona)
CORS(app)


class FinalPersona(db.Model):
    __tablename__ = 'finalpersona'

    interimPersona = db.Column(db.String(250), nullable=False, primary_key=True)
    likeTo = db.Column(db.String(250), nullable=False, primary_key=True)
    finalPersona = db.Column(db.String(250), nullable=False, primary_key=True)
    description = db.Column(db.String(500), nullable=False)
    quotes = db.Column(db.String(500), nullable=False)
    skills = db.Column(db.String(500), nullable=False)
    books = db.Column(db.String(250), nullable=False)

    def __init__(self, interimPersona, likeTo, finalPersona, description, quotes, persona):
        self.interimPersona = interimPersona
        self.likeTo = likeTo
        self.finalPersona = finalPersona
        self.description = description
        self.quotes = quotes
        self.skills = persona
        self.books = books

    def json(self):
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
# localhost:5002/get_all_final_personas
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

@app.route("/get_all_books")
def get_all_books():
    try:
        query = db.session.query(FinalPersona.books.distinct())
        
        return {
            'books': [
                FinalPersona[0] for FinalPersona in query.all()
            ]
        }, 200
    except Exception as e:
        print(e)
        return {"error" : "Cannot retrieve books"}, 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
