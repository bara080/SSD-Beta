# from flask import Blueprint, render_template, request, redirect, url_for, flash
# from flask_login import login_user, logout_user, login_required
# from app.models import Student
# from app import bcrypt

# student_bp = Blueprint('student', __name__)

# @student_bp.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         department = request.form['department']
#         hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
#         Student.create(username, hashed_password, department)
#         flash('Registration successful')
#         return redirect(url_for('student.portal'))
#     return render_template('student/register.html')

# @student_bp.route('/portal')
# @login_required
# def portal():
#     return render_template('student/portal.html')

# @student_bp.route('/schedule_appointment')
# @login_required
# def schedule_appointment():
#     return render_template('student/schedule_appointment.html')
