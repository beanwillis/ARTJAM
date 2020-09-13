from flask import Flask, render_template, redirect
from flask_cors import CORS
app = Flask(__name__)

CORS(app)

@app.route("/home")
def about():
    return render_template("home.html")

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

@app.route("/name")
def name():
    return render_template("name.html")

@app.route("/books")
def books():
    return render_template("books.html")

@app.route("/specificBook")
def specificBook():
    return render_template("specific-book.html")

@app.route("/avatar")
def avatar():
    return render_template("avatar.html")

@app.route("/confirm-avatar")
def confirmAvatar():
    return render_template("confirm-avatar.html")

@app.route("/home-activities")
def homeActivities():
    return render_template("activities-at-home.html")

@app.route("/campus-activities")
def campusActivities():
    return render_template("activities-at-campus.html")

@app.route("/digging-deeper")
def diggingDeeper():
    return render_template("digging-deeper.html")

@app.route("/final-report")
def finalReport():
    return render_template("final-report.html")

@app.route("/skill-recommendation")
def skillRecommendation():
    return render_template("skill-recommendation.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

# lsof -i:5000 then kill -QUIT <pid>