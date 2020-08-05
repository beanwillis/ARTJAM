from flask import Flask, render_template, redirect
from flask_cors import CORS
app = Flask(__name__)

CORS(app)

@app.route("/home")
def about():
    return render_template("home.html")

@app.route("/map")
def map():
    return render_template("map.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

# lsof -i:5000 then kill -QUIT <pid>