import os
from datetime import datetime, timezone
from dotenv import load_dotenv
from flask import Flask, request, render_template, session, redirect, url_for, flash, logging
from flask_bcrypt import Bcrypt
import psycopg2
from datetime import datetime
from wtforms import StringField, Form, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from app.config import Config


# Establish app connection
app = Flask(__name__)


# Initialize SQLAlchemy
# db = SQLAlchemy(app)

# Home route
@app.route('/')
def home():
    return render_template("home.html")

# Student profile route
@app.route('/signup')
def signup():
    # Implement logic to fetch and display student profile from db
    return render_template("signup.html")

# Student about profile
@app.route('/home')
def h():
    # Implement logic to display student about information
    return render_template("home.html")

# Student dashboard route
@app.route('/dashboard')
def dashboard():
    # Implement logic to display student dashboard information
    return render_template("dashboard.html")

# Student form route
@app.route('/register')
def register():
    # Implement logic to display student dashboard information
    return render_template("register.html")


# Student portal route
@app.route('/portal')
def portal():
    # Implement logic to display student dashboard information
    return render_template("portal.html")

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
