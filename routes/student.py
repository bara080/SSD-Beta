from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services.student_services import create_student, read_students, read_student, update_student, delete_student

student_bp = Blueprint('student', __name__)

@student_bp.route('/students')
def list_students():
    students = read_students()  # Implement reading all students
    return render_template('student/student_list.html', students=students)

@student_bp.route('/student/create', methods=['GET', 'POST'])
def create_student_view():
    if request.method == 'POST':
        # Extract form data
        student_data = {
            'first_name': request.form.get('first_name'),
            'last_name': request.form.get('last_name'),
            'initials': request.form.get('initials'),
            'job_title': request.form.get('job_title'),
            'department': request.form.get('department')
        }
        create_student(student_data)  # Call create_student function
        flash('Student created successfully!', 'success')
        return redirect(url_for('student.list_students'))
    return render_template('student/student_form.html')

@student_bp.route('/student/update/<int:id>', methods=['GET', 'POST'])
def update_student_view(id):
    student = read_student(id)
    if request.method == 'POST':
        # Extract form data
        student_data = {
            'first_name': request.form.get('first_name'),
            'last_name': request.form.get('last_name'),
            'initials': request.form.get('initials'),
            'job_title': request.form.get('job_title'),
            'department': request.form.get('department')
        }
        update_student(id, student_data)  # Call update_student function
        flash('Student updated successfully!', 'success')
        return redirect(url_for('student.list_students'))
    return render_template('student/student_form.html', student=student)

@student_bp.route('/student/delete/<int:id>', methods=['POST'])
def delete_student_view(id):
    delete_student(id)  # Call delete_student function
    flash('Student deleted successfully!', 'success')
    return redirect(url_for('student.list_students'))
