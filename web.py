# WebApp
from flask import Flask, render_template

app = Flask(__name__)

# Render Homepage
@app.route("/")
def index():
    title = 'Homepage'
    return render_template("index.html", title=title)


# Render About page
@app.route("/about")
def about():
    title = 'About'
    return render_template('about.html', title=title)


# Render contacts page
@app.route("/contact")
def contact():
    title = 'Contact'
    return render_template('contact.html', title=title)
