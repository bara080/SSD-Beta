import os
from datetime import datetime, timezone
from dotenv import load_dotenv
from flask import Flask, request, render_template, session, redirect, url_for, flash, logging
from flask_bcrypt import Bcrypt
from wtforms import StringField, Form, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from app.config import Config
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from app.models import Advisor, User, Department, Course, Grade
from app.routes.auth import auth_bp
from app.routes.advisor import advisor_bp


# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.config.from_object('app.config.Config')

# Initialize extensions
db = SQLAlchemy(app)
# db.init_app(app)
# migrate = Migrate()
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'


# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(advisor_bp)

# User loader for Flask-Login
# from app.models.user import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Configure LoginManager
# login_manager.login_view = 'auth.login'
# login_manager.login_message_category = 'info'

# app.register_blueprint(auth_bp)


# Home route
@app.route('/')
def home():
    return render_template("home.html")


# Student signup route
@app.route('/auth/signup', methods=['GET', 'POST'])
def signup():
    return render_template("auth.signup.html")


# Student dashboard route
@app.route('/portal')
def portal():
    return render_template("portal.html")


# Student dashboard route
@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

# Student register route
@app.route('/register')
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)