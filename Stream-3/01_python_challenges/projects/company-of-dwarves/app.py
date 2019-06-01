import os
import json
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "watch_a_secret"

# Home view
@app.route("/")

# Note if using url_for() method for hyperlinks, make sure that function name below
# matches the name passed to the method (ie print_hello_world)

def print_hello_world():
    return render_template("index.html", page_title = "Welcome to the home page")

    
# Media view
@app.route("/media")

def print_hello_media():
    with open('json/company.json') as dwarven_company_data:
        data = []
        data = json.load(dwarven_company_data)
        return render_template("media.html", page_title = "Welcome to the media page", dwarven_company = data)


# Media member view (for members in dwarven company)
@app.route("/media/<member_name>")

def about_member(member_name):
    member = {}
    with open('json/company.json') as dwarven_company_data:
        data = []
        data = json.load(dwarven_company_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
                
    return render_template("member.html", member = member)
    

# Projects view
@app.route("/projects")

def print_hello_projects():
    return render_template("projects.html", page_title = "Welcome to the projects page")
    
    
# Contact view

# Note: methods other than GET need to be specified when using flask
@app.route("/contact", methods = ["GET", "POST"])

def print_hello_contact():
    if request.method == "POST":
        print ("Receiving posts ...")
        # Return the name posted using the contact form and use flash to provide user feedback
        flash("Thanks for your message {}".format(request.form["name"]))
    return render_template("contact.html", page_title = "Welcome to the contact page")
    

# Configuration
if __name__ == "__main__":
    app.run(host = os.environ.get("IP"), port = int(os.environ.get("PORT")), 
        # Need debug in order to view changes made in the browser
        debug = True)