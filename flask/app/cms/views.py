import os

from flask import render_template

from app import app, mongo


@app.route("/")
def index():
    online_users = mongo.db.users.find({"online": True})
    return render_template("index.html", online_users=online_users)
