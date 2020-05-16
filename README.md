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

### Make life easier on yourself with debug mode 
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