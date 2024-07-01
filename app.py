import os
from datetime import datetime, timezone
from dotenv import load_dotenv
from flask import Flask, request, render_template, session, redirect, url_for, flash, logging
from pymongo import MongoClient
from config import mongo_connectdb
from wtforms import StringField, Form, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

# Establish app connection
app = Flask(__name__)

# Establish MongoDB connection
db = mongo_connectdb()

# Home route
@app.route('/')
def home():
    return render_template("home.html")

# Student profile route
@app.route('/profile')
def profile():
    # Implement logic to fetch and display student profile from db
    return render_template("profile.html")

# Student about profile
@app.route('/about')
def about():
    # Implement logic to display student about information
    return render_template("about.html")

# Student dashboard route
@app.route('/dashboard')
def dashboard():
    # Implement logic to display student dashboard information
    return render_template("dashboard.html")

# Student form route
@app.route('/form')
def form():
    # Implement logic to display student dashboard information
    return render_template("form.html")

class RegistrationForm(Form):
    name = StringField("Name", [validators.length(min=1, max=50)])
    username = StringField("Username", [validators.length(min=5, max=100)])
    email = StringField("Email", [validators.length(min=5, max=100)])
    password = PasswordField("Password", [
        validators.DataRequired(),
        validators.EqualTo("confirm", message="Passwords do not match")
    ])
    confirm = PasswordField("Confirm Password")

if __name__ == "__main__":
    app.run(debug=True)
