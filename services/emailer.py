from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
import smtplib
import imghdr
import email
# import services.config
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from email.message import EmailMessage

app = Flask(__name__)

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "artjam-287602-c4a440e2da91.json"

cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
    "projectId": "artjam-287602"
})

db = firestore.client()

# Allow Cross-Origin Resource Sharing making AJAX response possible (Accessing microservice via browser using WAMP/MAMP will cause CORS interimPersona)
CORS(app)


def sendReport(emailAddress, personaType):

    book_data = []
    skill_data = []
    data = []
    try:

        persona_ref = db.collection(u"FinalPersona")
        persona_docs = persona_ref.where(
            "finalPersona", "==", personaType).stream()

        final_ref = db.collection(u"Books")

        books = ""
        for doc in persona_docs:
            data = doc.to_dict()
            books = data["books"]

        book_list = books.split(",")
        book_details = []

        for b in book_list:
            book_docs = final_ref.where("id", "==", b).stream()
            for b_doc in book_docs:
                book_details.append(b_doc.to_dict())

        book_data = book_details

        final_ref = db.collection(u"Skills")

        skills = ""
        skills = data["skills"]
        skill_list = skills.split(",")
        skill_details = []
        for b in skill_list:
            skill_docs = final_ref.where("id", "==", b).stream()
            for b_doc in skill_docs:
                skill_details.append(b_doc.to_dict())

        skill_data = skill_details

    except Exception as e:
        print(e)
        return {"error": "Cannot retrieve final personas"}, 500

    description = data["description"]

    print(book_data)
    print()
    print(skill_data)
    print()
    print(data)


    book_code = ""
    for book in book_data:
        code = """
            <div class="row">
                <div class="col">
                    <img width="150px" style="margin:auto; margin-top: 20px;" src='"""+ book["image_link"] +"""'>
                </div>
                <div class="col" style="margin-left: -100px;">
                    <h5>"""+book["name"]+"""</h5>
                    <p>"""+book["description"]+"""</p>  
                </div>
            </div>
            <br>
        """
        book_code += code


    skills_code = ""
    for skill in skill_data:
        code = """
            <tr>
                <td>"""+skill["name"]+"""</td>
                <td>"""+skill["quote"]+"""</td>
                <td>"""+skill["description"]+"""</td>
            </tr>
        """


    msg = EmailMessage()
    msg['Subject'] = 'Your Changemaking Journey - SMU'
    msg['From'] = services.config.EMAIL_ADDRESS
    msg['To'] = emailAddress
    # msg['To'] = 'beankhin1310@gmail.com'

    # msg.set_content('This is a plain text email')

    msg.add_alternative("""\
    <!DOCTYPE html>
    <html lang="en" style="height:100%;">
    <head>
        <meta charset="utf-8" />
        <meta
        name="viewport"
        content="width=device-width, initial-scale=1, shrink-to-fit=no"
        />
        <link rel="stylesheet" href="https://pro.fontawesome.com/releases/v5.10.0/css/all.css" integrity="sha384-AYmEC3Yw5cVb3ZcuHtOA93w35dYTsvhLPVnYs9eStHfGJvOvKxVfELGroGkvsg+p" crossorigin="anonymous"/>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    </head>
    <body>

        <div class="container">
            <div class="row">
                <div class="col" align="center" >
                    <br>
                    <img width="1000px" style="margin-left: -60px;" src="../static/img/misc/smu-header.PNG">
                </div>
                <div class="col">
                    <h4 class="text-center">
                        <br><br>Thank you for travelling with us on this Changemaking Journey!<br>
                        Your Changemaker Persona is <strong>"""+ personaType +"""</strong>
                    </h4>
                </div>
            </div>
            <div class="row">
                <div class="col">
                    <img width="500px" style="margin-top: -150px; margin-left: -50px;" src="../static/img/avatar-bodies/avatar-4-CEO-skin-1.svg">
                </div>
                <div class="col" align="center" >
                    <div class="text-left" style="margin-left: -40px;">
                        <h4><br><br>Description</h4>
                        <p>
                            """+ description +"""
                            <br><br>
                        </p>
                        <h4>Recommended Books</h4>
                        <br>
                        
                        <div class="container">
                            """+ book_code + """
                        </div>
                        
                    </div>
                </div>
            </div>

            <div class="row" >
                <div class="col" >
                    <h4>Recommended Skills</h4>
                    <table class="table">
                        <tr>
                            <th>Skill</th>
                            <th>Quotes</th>
                            <th>Description</th>
                        </tr>
                        """+ skills_code + """
                    </table>
                </div>
            </div>

            <div class="row">
                <div class="col text-center">
                    <br><br>
                    <p class="text-muted">Follow us on social media for the latest updates:</p>
                    <a class="btn-floating btn-tw" type="button" role="button" href="http://facebook.com/sgsmu" target="_blank"><i class="fab fa-facebook-f"></i></a>
                    <a class="btn-floating btn-tw" type="button" role="button" href="https://www.instagram.com/sgsmu" target="_blank"><i class="fab fa-instagram"></i></a>
                    <a class="btn-floating btn-tw" type="button" role="button" href="https://lcsi.smu.edu.sg/" target="_blank"><i class="fas fa-globe"></i></a>
                    <p class="text-muted">Copyright © 2020 Singapore Management University, All rights reserved.
                        You are receiving this email because you are a valued member of the social innovation ecosystem</p>
                    <br>
                </div>
            </div>
            
        </div>

    </body>

    </html>
    """, subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(services.config.EMAIL_ADDRESS,
                   services.config.EMAIL_PASSWORD)
        smtp.send_message(msg)
        smtp.quit()

    # return 200

sendReport("t", "CEO")