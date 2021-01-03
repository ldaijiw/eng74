from flask import Flask, jsonify, redirect, url_for, render_template, request, session
# create an instance of our app, with __name__ passed as arg

app = Flask(__name__)

students = [
    {"id": 0, "title": "Mr.", "first_name": "Leo", "last_name": "Waltmann", "course": "DevOps"}
]

# use decorator to create API/url for user to access our data in the browser
# single forward slash indicates home (localhost:5000 is default port for Flask)
@app.route("/")
def home():
    return render_template("home.html")
# this function will run when the URL/API is accessed


# Creating our own API to display data on the specific route/URL/Endpoint/API
# will add URL to http://127.0.0.1:5000/api/v1/student/data
@app.route("/api/v1/student/data", methods = ["GET"])
def customised_api():
    # Extact Transform Load
    # Transforms data into JSON
    return jsonify(students)


@app.route("/welcome/")
def greet_user():
    return "Welcome to eng74"


# module to redirect user back to specific page
@app.route("/redirectme/")
def redirect_me():
    return redirect(url_for(greet_user))

# if any error occurs then redirects to error message page
@app.errorhandler(Exception)
def error_occured(error):
    return redirect(url_for("error_message"))

@app.route("/error/")
def error_message():
    return render_template("error.html")

# taking arguments
@app.route("/user/<username>/")
def welcome_user(username):
    return f"Welcome {username}"


@app.route("/index/")
def index():
    return render_template("index.html")


users = []
users.append({"user_id": 1, "username": "ldaijiw", "password": "test"})
users.append({"user_id": 2, "username": "admin", "password": "admin"})

@app.route("/login/", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        print("POST")
        #session.pop('user_id')
        username = request.form['username']
        password = request.form['password']

        print(users)
        print(username)
        print(password)
        user = [x for x in users if x["username"] == username][0]

        print(user)

        if user and user["password"] == password:
            print(username)
            # session['user_id'] = user.user_id
            return redirect('/user/admin/')

        return redirect(url_for('login'))

    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)