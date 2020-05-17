# Rendering HTML Template
# render-template method
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# Render about page
@app.route("/about")
def about():
    return render_template('about.html')