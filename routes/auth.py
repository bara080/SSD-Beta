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
            flash('Please fill out all fields.', 'warning')
            return render_template('auth/signup.html')

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, password=hashed_password, email=email)

        try:
            db.session.add(new_user)
            db.session.commit()
            print(f"New user created: {username}, {email}")
            flash('Account created successfully!', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            db.session.rollback()
            print(f"Error: {e}")
            flash('Error creating account. Please try again.', 'danger')

    return render_template('auth/signup.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        print(f"Login attempt: {email}, Password: {'provided' if password else 'not provided'}")

        if not email or not password:
            print("Email or password not provided.")
            flash('Invalid email or password', 'danger')
            return redirect(url_for('auth.login'))  # Redirect to avoid form resubmission on refresh

        user = User.query.filter_by(email=email).first()
        print(f"Retrieved user: {user}")

        if user:
            print(f"User found: {user.email}")
            password_check = bcrypt.check_password_hash(user.password, password)
            print(f"Password check result: {password_check}")

            if password_check:
                print("Password check passed.")
                login_user(user)
                flash('Logged in successfully!', 'success')
                return redirect(url_for('portal'))
            else:
                print("Invalid password.")
                flash('Invalid email or password', 'danger')
        else:
            print("User not found.")
            flash('Invalid email or password', 'danger')

    return render_template('auth/login.html')


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('auth.login'))