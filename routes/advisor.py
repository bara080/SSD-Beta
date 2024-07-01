# from flask import Blueprint, render_template, request, redirect, url_for, flash
# from flask_login import login_user, logout_user, login_required
# from app.models import Advisor
# from app import bcrypt

# advisor_bp = Blueprint('advisor', __name__)

# @advisor_bp.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         advisor = Advisor.get_by_username(username)
#         if advisor and bcrypt.check_password_hash(advisor['password'], password):
#             login_user(Advisor(username, advisor['password']))
#             return redirect(url_for('advisor.dashboard'))
#         else:
#             flash('Invalid username or password')
#     return render_template('advisor/login.html')

# @advisor_bp.route('/dashboard')
# @login_required
# def dashboard():
#     return render_template('advisor/dashboard.html')

# @advisor_bp.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('advisor.login'))
