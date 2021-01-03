# MVC with Flask in Python

## Model View Controller

MVC is a framework used for web development

![](images/mvc.jpg)

- The user is shown the front end, displayed any data in the browser using HTML, CSS, JS.
- The user makes a request to the _controller_ which in turn requests information from the database (_model_). - - The _model_ then sends the information back to the  _controller_
- The controller then sends the data to the _view_ which displays the response back to the user.

**MODEL**

- Using SQL Database

**VIEW**

- View in browser using HTML (Hyper Text Markup Language), CSS (Cascading Style Sheet), Javascript, and Bootstrap

**CONTROLLER**

- Using Python Flask


**Building our API**

- Display data from Python Flask to specific API call/URL/endpoint


## Flask

**Why Flask?**

- Flask is a web framework, a set of tools to build a web application
- It's very powerful to interact with the DB and user interface/browser
- Used to create an API
- Allows to integrate with HTML, CSS, JS
- Allows to map HTTP requests to Python functions
- Allows to set API path as a URL to view in the browser

### Setup

- Ensure it is installed with ``pip install flask``
- Import with
```python
from flask import Flask, jsonify, redirect, url_for
```
- Run the flask app with ``flask run``
- Initialise the flask with
```python
app = Flask(__name__)
```

### Flask Features

**JSONIFY**
- Return JSON with ``jsonify``
```python
students = [
    {"id": 0, "title": "Mr.", "first_name": "Leo", "last_name": "Waltmann", "course": "DevOps"}
]
@app.route("/api/v1/student/data", methods = ["GET"])
def customised_api():
    # Extact Transform Load
    # Transforms data into JSON
    return jsonify(students)


```
**REDIRECT and URL_FOR**
- Redirects to different url
- Use ``url_for`` to refer to the function instead of typing out the whole URL
```python
@app.route("/redirectme/")
def redirect_me():
    return redirect(url_for(greet_user))
```

**ERROR REDIRECTING**
- Use ``app.errorhandler(Exception)`` to redirect to a given page in case of any errors
```python
# if any error occurs then redirects to error message page
@app.errorhandler(Exception)
def error_occured(error):
    return redirect(url_for(error_message))

@app.route("/error/")
def error_message():
    return "An error occurred, sorry"
```

**PASSING ARGUMENTS**
- Can pass arguments with <> in url which then passes argument to function
```python
# taking arguments
@app.route("/user/<username>/")
def welcome_user(username):
    return f"Welcome {username}"
```

### Using HTML

- Naming conventions are essential
- Require to create a template folder in directory
- Flask looks for templates folder and anything inside the folder 
- Create index html inside templates folder


**USING BOOTSTRAP**
- 


create a base.html file in templates folder
copy index.html to base.html
google how to extend code from base.html to index.html
Create text boxes for login form

