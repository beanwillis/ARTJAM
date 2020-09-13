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

@app.route("/get_all_interim_personas")
def get_all_interim_personas():
    interim_ref = db.collection(u"InterimPersona")
    docs = interim_ref.stream()

    persona_list = []
    for doc in docs:
        persona_list.append(doc.to_dict())
    
    try:
        return {
            'interim personas': persona_list
        }, 200
    except Exception as e:
        print(e)
        return {"error": "Cannot retrieve interim personas"}, 500

@app.route("/get_all_skills")
def get_all_skills():
    interim_ref = db.collection(u"InterimPersona")
    docs = interim_ref.stream()

    persona_list = set()
    for doc in docs:
        persona_list.add(doc.to_dict()["skills"])
    
    try:
        return {
            'skills': list(persona_list)
        }, 200
    except Exception as e:
        print(e)
        return {"error": "Cannot retrieve interim personas"}, 500

@app.route("/get_all_home_activities")
def get_all_home_activities():
    interim_ref = db.collection(u"InterimPersona")
    docs = interim_ref.stream()

    persona_list = set()
    for doc in docs:
        persona_list.add(doc.to_dict()["activities"])
    
    try:
        return {
            'skills': list(persona_list)
        }, 200
    except Exception as e:
        print(e)
        return {"error": "Cannot retrieve interim personas"}, 500

@app.route("/get_home_activities_by_wheel/<string:issue>/<string:skill>/<string:interest>")
def get_home_activities_by_wheel(issue, skill, interest):
    interim_ref = db.collection(u"InterimPersona")
    docs = interim_ref.where("issues", "==", issue).where("skills", "==", skill).where("interests", "==", interest).stream()

    try:
        activities = ""
        for doc in docs:
            activities = doc.to_dict()["activities"]

        return {
            'activities': activities
        }, 200
    except Exception as e:
        print(e)
        return {"error": "Cannot retrieve interim personas"}, 500

@app.route("/get_campus_activities_by_wheel/<string:issue>/<string:skill>/<string:interest>")
def get_campus_activities_by_wheel(issue, skill, interest):
    interim_ref = db.collection(u"InterimPersona")
    docs = interim_ref.where("issues", "==", issue).where("skills", "==", skill).where("interests", "==", interest).stream()

    try:
        activities = ""
        for doc in docs:
            activities = doc.to_dict()["schoolActivities"]

        return {
            'schoolActivities': activities
        }, 200
    except Exception as e:
        print(e)
        return {"error": "Cannot retrieve interim personas"}, 500
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)