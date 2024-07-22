from datetime import datetime, timezone
from flask import Flask, request, render_template, session, redirect, url_for, flash, logging,jsonify
# from flask_bcrypt import Bcrypt
from wtforms import StringField, Form, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from app.config import Config
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_login import LoginManager
from dotenv import load_dotenv
import os


# Load environment variables
load_dotenv()

# Initialize extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()
login_manager = LoginManager()
def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    # def get_income_vs_expense_data():
    #     income_vs_expense = [500, 1000]
    #     # Function to fetch or calculate income_vs_expense data
    #     return [1000, 1500]  # Example data
    
    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    
    with app.app_context():
        from app.models import Advisor, User, Department, Course, Grade
        db.create_all()
        print("Database tables created successfully.")

    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'

    # Register blueprints
    from app.routes.auth import auth_bp
    from app.routes.advisor import advisor_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(advisor_bp)

    # Register user loader
    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register routes
    @app.route('/')
    def home():

        return render_template("home.html")

    @app.route('/auth/signup', methods=['GET', 'POST'])
    def signup():
        return render_template("auth/signup.html")

    @app.route('/portal')
    def portal():
        return render_template("portal.html")
    
    @app.route('/dashboard')
    def dashboard():
        income_vs_expense = [500, 1000]  # Example data
        income_category = [200, 300, 400, 100]  # Example data
        over_time_expenditure = [150, 200, 250, 300, 350]  # Example data
        dates_label = ["January", "February", "March", "April", "May"]  # Example labels

        return render_template('dashboard.html',
                               income_vs_expense=income_vs_expense,
                               income_category=income_category,
                               over_time_expenditure=over_time_expenditure,
                               dates_label=dates_label)

    @app.route('/register')
    def register():
        return render_template("register.html")

    return app
