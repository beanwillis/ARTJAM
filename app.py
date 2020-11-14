from flask import Flask, render_template, redirect
from flask_cors import CORS

# from services.emailer import sendReport

app = Flask(__name__)

CORS(app)

@app.route("/laptop-home")
def laptopHome():
    return render_template("laptop-home.html")

@app.route("/home")
def about():
    return render_template("home.html")

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

@app.route("/info")
def info():
    return render_template("info.html")

@app.route("/name")
def name():
    return render_template("name.html")

@app.route("/books")
def books():
    return render_template("books.html")

@app.route("/specificBook")
def specificBook():
    return render_template("specific-book.html")

@app.route("/specific-book-recommendation")
def specificBookRecommendation():
    return render_template("specific-book-recommendation.html")

@app.route("/avatar")
def avatar():
    return render_template("avatar.html")

@app.route("/confirm-avatar")
def confirmAvatar():
    return render_template("confirm-avatar.html")

@app.route("/interest")
def interest():
    return render_template("interest.html")

@app.route("/skill")
def skill():
    return render_template("skill.html")

@app.route("/issue")
def issue():
    return render_template("issue.html")

@app.route("/home-activities")
def homeActivities():
    return render_template("activities-at-home.html")

@app.route("/campus-activities")
def campusActivities():
    return render_template("activities-at-campus.html")

@app.route("/digging-deeper")
def diggingDeeper():
    return render_template("digging-deeper.html")

@app.route("/ascend")
def ascend():
    return render_template("ascend.html")

@app.route("/final-report")
def finalReport():
    return render_template("final-report.html")

@app.route("/skill-recommendation")
def skillRecommendation():
    return render_template("skill-recommendation.html")

@app.route("/book-recommendation")
def bookRecommendation():
    return render_template("book-recommendation.html")

@app.route("/other-resource")
def otherResource():
    return render_template("other-resource.html")

@app.route("/thank-you")
def thankYou():
    return render_template("thank-you.html")

@app.route("/map")
def map():
    return render_template("map.html")

@app.route("/emailReport/<string:emailAddress>/<string:personaType>")
def emailReport(emailAddress, personaType):
    sendReport(emailAddress, personaType)
    return render_template("thank-you.html", emailed="emailed")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

# lsof -i:5000 then kill -QUIT <pid>