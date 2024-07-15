# TODO : Import all necessary flask libraries
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from app.models.user import User
from app import db, bcrypt

from flask import Blueprint, request, redirect, url_for, flash, render_template
from flask_login import login_user
from app import db, bcrypt
from app.models.user import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')

        print(f"Signup attempt: {username}, {email}")

        if not username or not password or not email:
            print("Form data is missing.")
            flash('Please fill out all fields.')
            return render_template('signup.html')

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, password=hashed_password, email=email)

        try:
            db.session.add(new_user)
            db.session.commit()
            print(f"New user created: {username}, {email}")
            flash('Account created successfully!')
            return redirect(url_for('auth.login'))
        except Exception as e:
            db.session.rollback()
            print(f"Error: {e}")
            flash('Error creating account. Please try again.')

    return render_template('signup.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        print(f"Login attempt: {username}, Password: {'provided' if password else 'not provided'}")

        if not username or not password:
            print("Username or password not provided.")
            flash('Invalid username or password', 'danger')
            return render_template('login.html')

        user = User.query.filter_by(username=username).first()
        print(f"Retrieved user: {user}")

        if user:
            print(f"User found: {user.username}")
            password_check = bcrypt.check_password_hash(user.password, password)
            print(f"Password check result: {password_check}")

            if password_check:
                print("Password check passed.")
                login_user(user)
                flash('Logged in successfully!', 'success')
                return redirect(url_for('portal'))  # replace with your protected route
            else:
                print("Invalid password.")
                flash('Invalid username or password', 'danger')
        else:
            print("User not found.")
            flash('Invalid username or password', 'danger')

    return render_template('login.html')



# logout route
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('auth.login'))
