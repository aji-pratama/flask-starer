import os

from flask import render_template

from app import app, mongo


@app.route("/<email>")
def index(email):
    online_users = mongo.db.users.find_one_or_404({"email": email})
    return render_template("index.html", online_users=online_users)
