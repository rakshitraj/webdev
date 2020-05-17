# WebApp
from flask import Flask, render_template
app = Flask(__name__)

# Render Homepage
@app.route("/")
def index():
    return render_template("index.html")

# Render About page
@app.route("/about")
def about():
    return render_template('about.html')

# Render contacts page
@app.route("/contact")
def contact():
    return render_template('contact.html')