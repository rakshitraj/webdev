# Web Development using Flask
### What is Flask?
Flask is a light-weight framework with a built-in server that will allow us to turn our Python scripts into webpages and web apps. To say that another way, Flask allows us to make websites with Python. 

### Let's see if Flask is installed
If you used Anaconda to install Python then you should have Flask installed already. 

To find out if you have flask type the following command on the command line: 

```python3
$ Flask
 ```

If the text that appears says something like "A general utility script for Flask applications" and "Options" then you are good to go!

But if you see "command not found?" then you'll want to visit the Flask homepage and install Flask by running the command 
```python3
pip install flask 
```

### Let's run our Flask server 
Find the starter code on the [Flask homepage](https://flask.palletsprojects.com/en/1.1.x/). Paste that code into a new file called `hello.py`.

```python3
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
```

Run the server with the command 
This command will run your Python script and more or less turn your command line application into a server.
```python3
$ FLASK_APP=hello.py flask run
```
To quit the server you'll need to press `control-Z`.

### debug mode 
Every time you make a change in you're Python code, you'll have quit, and restart the server. Annoying right? Run `export FLASK_ENV` command and your Python code will update in real-time, without having to restart: 
```bash
$ export FLASK_ENV=development
```
Alternatively you could also try
```bash
$ export FLASK_ENV=1  // set environment to development , debug mode
```
To unset the debug mode
```bash
$ export FLASK_ENV=1  // unset debug mode
```
If for some reason that didn't work, try adding these two lines to the bottom of your file: 
```python3
if __name__=="_main_":
    app.run(debug=True)
```
Note: The first time you add this code you'll need to shut down the Flask server and restart it.

### Rendering HTML Templates

Create file `web.py` similar to `hello.py' and update the route file with the `render_template` method.
```python3
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
```
Create a folder named `templates` located in the same directory as `web.py`.
 The `render_templates` function always looks for templates under the `templates` folder.
 
 Inside the `templates` folder create `index.html` loaded with some placeholder html.
 ```html
<html>
    <head>
        <title>Flask App</title>
    </head>
    <body>
        <h1>Hello I'm HTLM</h1>
    </body>
</html>
```
Now run the file using
```bash
$ export FLASK_ENV=1            # set debug mode
$ FLASK_APP=web.py flask run    # run the app
```

### How to serve new pages in Flask
Now that we have out 'Homepage' up and running, it is time to include and serve other pages in our web app.
We are going to serve an 'About' page. To do this, we create a new `html` file in the `templates` folder called `about.html` which will contain somthing like 
```html
<html>
    <head>
        <title>About Page</title>
    </head>
    <body>
        <h1>Hello, I am just chilling about!</h1>
        <a href="/">Homepage</a>
        <a href="/about">About</a>
    </body>>
        <a href="/about">About</a>
</html>
```
These lines of code, will add navigational ablities by providing hyperlinks to the 'About' page and the 'Homepage'
```html
 <a href="/">Homepage</a>
 <a href="/about">About</a>
```
Therefore, we copy these lines to `index.html` as well. In the future we will use an include-lines feature
to includes certain parts of html across pages, since IRL projects will have way too many pages for copy-pasting html to be practical.

##### Serving the page
To seve the page we add the following lines to `web.py` to set a route to the about page.

```python3
# Render about page
@app.route("/about")
def about():
    return render_template('about.html')
```
`web.py` now looks like

```python3
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
```
### Flask includes

`includes` allows us to create reusable snippets of code and add to all pages where it is required.
This helps us to easily maintain the pages and reduces chances of error while update pages

#### 1. Create header and footer includes

_index.html_
```html
{% include 'header.html' %}

        <h1>Hello I'm HTLM</h1>

{% include 'footer.html' %}
```
#### 2. Move the head of your HTML to header.html
Create `templates/header.html`, and add header 
```html
<html>
    <head>
        <title>Homepage</title>
    </head>
    <body>
        <a href="/">Homepage</a>
        <a href="/about">About</a>
        <a href="/contact">Contact</a>
```
#### 3. Move the foot of your HTML to footer.html
Create `templates/footer.html`, and add footer 
```html
    </body>
</html>
```