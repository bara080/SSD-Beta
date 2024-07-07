from flask import Blueprint, render_template, request, redirect, url_for
from app.services.advisor_services import create_advisor, read_advisor, update_advisor, delete_advisor
from app.models.advisor import Advisor
from app import db

advisor_bp = Blueprint('advisor', __name__)

@advisor_bp.route('/advisors')
def list_advisors():
    advisors = Advisor.query.all()
    return render_template('advisor/advisors.html', advisors=advisors)

@advisor_bp.route('/advisor/create', methods=['GET', 'POST'])
def create_advisor_view():
    if request.method == 'POST':
        advisor = Advisor(
            advisorID=request.form['advisorID'],
            lastName=request.form['lastName'],
            firstName=request.form['firstName'],
            initials=request.form['initials'],
            jobTitle=request.form['jobTitle'],
            department=request.form['department']
        )
        db.session.add(advisor)
        db.session.commit()
        return redirect(url_for('advisor.list_advisors'))
    return render_template('advisor/create_advisor.html')

@advisor_bp.route('/advisor/update/<advisorID>', methods=['GET', 'POST'])
def update_advisor_view(advisorID):
    advisor = Advisor.query.get(advisorID)
    if request.method == 'POST':
        advisor.lastName = request.form['lastName']
        advisor.firstName = request.form['firstName']
        advisor.initials = request.form['initials']
        advisor.jobTitle = request.form['jobTitle']
        advisor.department = request.form['department']
        db.session.commit()
        return redirect(url_for('advisor.list_advisors'))
    return render_template('advisor/update_advisor.html', advisor=advisor)

@advisor_bp.route('/advisor/delete/<advisorID>', methods=['POST'])
def delete_advisor_view(advisorID):
    advisor = Advisor.query.get(advisorID)
    db.session.delete(advisor)
    db.session.commit()
    return redirect(url_for('advisor.list_advisors'))
