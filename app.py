# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/shop")
def shop():
    return render_template("shop.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route("/track")
def track():
    return render_template("track.html")

@app.route("/feedback")
def feedback():
    return render_template("feedback.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/vision")
def vision():
    return render_template("vision.html")

@app.route('/categories')
def categories():
    return render_template('categories.html')


if __name__ == "__main__":
    app.run(debug=True)
