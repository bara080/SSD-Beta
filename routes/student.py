from flask import Blueprint, render_template, request, redirect, url_for
from app.services.student_service import create_student, read_student, update_student, delete_student

student_bp = Blueprint('student', __name__)

@student_bp.route('/students')
def list_students():
    # Implement reading all students
    return render_template('student/student_list.html')

@student_bp.route('/student/create', methods=['GET', 'POST'])
def create_student_view():
    if request.method == 'POST':
        # Extract form data and call create_student function
        return redirect(url_for('student.list_students'))
    return render_template('student/student_form.html')

# Additional routes for update and delete as needed
