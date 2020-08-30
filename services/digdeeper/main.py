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

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "artjam-287602-690502438d19.json"

cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
    "projectId": "artjam-287602"
})

db = firestore.client()

# Allow Cross-Origin Resource Sharing making AJAX response possible (Accessing microservice via browser using WAMP/MAMP will cause CORS interimPersona)
CORS(app)

@app.route("/get_all")
def get_all():

    dd_ref = db.collection(u"DigDeeper")
    docs = dd_ref.stream()

    dd_list = []
    for doc in docs:
        dd_list.append(doc.to_dict())
    
    try:
        return {
            'data': dd_list
        }, 200
    except Exception as e:
        print(e)
        return {"error": "Cannot retrieve final personas"}, 500

@app.route("/get_iLikeTo")
def get_iLikeTo():
    dd_ref = db.collection(u"DigDeeper")
    docs = dd_ref.stream()

    dd_list = []
    for doc in docs:
        dd_list.append(doc.to_dict()["iLikeTo"])
    
    try:
        return {
            'data': dd_list
        }, 200
    except Exception as e:
        print(e)
        return {"error": "Cannot retrieve final personas"}, 500
        
@app.route("/get_dig_deeper_desc/<string:iLikeTo>")
def get_desc_by_ilt(iLikeTo):
    dd_ref = db.collection(u"DigDeeper")
    docs = dd_ref.where("iLikeTo", "==", iLikeTo).stream()

    try:
        for doc in docs:
            return {
                'data': doc.to_dict()
            }, 200
        
    except Exception as e:
        print(e)
        return {"error": "Cannot retrieve final personas"}, 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
