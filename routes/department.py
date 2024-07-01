# from flask import Blueprint, render_template
# from app.models import Department

# department_bp = Blueprint('department', __name__)

# @department_bp.route('/')
# def list_departments():
#     departments = Department.get_all()
#     return render_template('department/list.html', departments=departments)

# @department_bp.route('/<name>')
# def department_detail(name):
#     department = Department.get_by_name(name)
#     return render_template('department/detail.html', department=department)
