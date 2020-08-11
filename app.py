from flask import Flask, render_template, redirect
from flask_cors import CORS
app = Flask(__name__)

CORS(app)

@app.route("/home")
def about():
    return render_template("home.html")


@app.route("/books")
def books():
    return render_template("books.html")

@app.route("/avatar")
def avatar():
    return render_template("avatar.html")

@app.route("/home-activities")
def homeActivities():
    return render_template("activities-at-home.html")

@app.route("/campus-activities")
def campusActivities():
    return render_template("activities-at-campus.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

# lsof -i:5000 then kill -QUIT <pid>