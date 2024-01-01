from flask import Flask, render_template, redirect, jsonify


app = Flask(__name__)


jobs = [

    {   'id': 1,
        'title': "Data Scientist",
        'location': "Addis Ababa",
        'salary': "15,000 USD"
    },

     {   'id': 2,
        'title': "Data entry specialist",
        'location': "Addis Ababa",
        'salary': "11,000 USD"
    },

     {   'id': 3,
        'title': "Data Scientist",
        'location': "Bahirdar",
        'salary': "12,000 USD"
    },

     {   'id': 4,
        'title': "Data Scientist",
        'location': "Addis Ababa",
        'salary': "15,000 USD"
    },

     {   'id': 5,
        'title': "Software Engineer",
        'location': "Dire dawa",
        'salary': "15,000 USD"
    },

]

# Redirect homepage to '/home'
@app.route("/")
def index_page():
    return redirect("/home")

# Homepage
@app.route("/home")
def home_page():
    return render_template("index.html", jobs=jobs)

# About page for keydama careers site
@app.route("/about")
def about():
    return "About me? what do you wanna learn?"


@app.route("/api/jobs")
def json_jobs():
    return  jsonify(jobs)

if __name__ == "__main__":
    app.run()
