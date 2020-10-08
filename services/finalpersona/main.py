from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

app = Flask(__name__)

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "artjam-287602-c4a440e2da91.json"

cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
    "projectId": "artjam-287602"
})

db = firestore.client()

# Allow Cross-Origin Resource Sharing making AJAX response possible (Accessing microservice via browser using WAMP/MAMP will cause CORS interimPersona)
CORS(app)

@app.route("/get_all_final_personas")
# localhost:5002/get_all_final_personas
def get_all_final_personas():

    final_ref = db.collection(u"FinalPersona")
    docs = final_ref.stream()

    persona_list = []
    for doc in docs:
        persona_list.append(doc.to_dict())
    
    try:
        return {
            'final personas': persona_list
        }, 200
    except Exception as e:
        print(e)
        return {"error": "Cannot retrieve final personas"}, 500

@app.route("/get_final_persona/<string:interimPersona>/<string:likeTo>")
def get_final_persona(likeTo, interimPersona):
    final_ref = db.collection(u"FinalPersona")
    docs = final_ref.where("likeTo", "==", likeTo).where("interimPersona", "==", interimPersona).stream()
    
    try:
        for doc in docs:
            return {
                'data': doc.to_dict()
            }, 200
        
    except Exception as e:
        print(e)
        return {"error": "Cannot retrieve final personas"}, 500

@app.route("/get_all_books")
def get_all_books():
    final_ref = db.collection(u"Books")
    docs = final_ref.stream()

    book_list = []
    for doc in docs:
        book_list.append(doc.to_dict())
    
    try:
        return {
            'books': book_list
        }, 200
    except Exception as e:
        print(e)
        return {"error": "Cannot retrieve books"}, 500

@app.route("/get_books_by_final_persona/<string:finalPersona>")
def get_books_by_final_persona(finalPersona):

    persona_ref = db.collection(u"FinalPersona")
    persona_docs = persona_ref.where("finalPersona", "==", finalPersona).stream()

    final_ref = db.collection(u"Books")

    books = ""
    try:
        for doc in persona_docs:
            books = doc.to_dict()["books"]

        book_list = books.split(",")
        for b in book_list:
            b.replace("\\n", " ")

        book_details = []

        for b in book_list:
            book_docs = final_ref.where("name", "==", b).stream()
            for b_doc in book_docs:
                book_details.append(b_doc.to_dict())

        return {
            "books" : book_details
        }, 200
    except Exception as e:
        print(e)
        return {"error" : "Cannot retrieve book"}, 500


@app.route("/get_all_skills")
def get_all_skills():
    final_ref = db.collection(u"Skills")
    docs = final_ref.stream()

    persona_list = []
    for doc in docs:
        # print(doc)
        persona_list.append(doc.to_dict())
    
    try:
        return {
            'skills': persona_list
        }, 200
    except Exception as e:
        print(e)
        return {"error": "Cannot retrieve skills"}, 500

@app.route("/get_skills_by_final_persona/<string:finalPersona>")
def get_skills_by_final_persona(finalPersona):

    persona_ref = db.collection(u"FinalPersona")
    persona_docs = persona_ref.where("finalPersona", "==", finalPersona).stream()

    final_ref = db.collection(u"Skills")

    skills = ""
    try:
        for doc in persona_docs:
            skills = doc.to_dict()["skills"]

        skill_list = skills.split(",")
        skill_details = []
        for b in skill_list:
            skill_docs = final_ref.where("Skills", "==", b).stream()
            for b_doc in skill_docs:
                skill_details.append(b_doc.to_dict())

        return {
            "skills" : skill_details
        }, 200
    except Exception as e:
        print(e)
        return {"error" : "Cannot retrieve book"}, 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
