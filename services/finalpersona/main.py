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


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
