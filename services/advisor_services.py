from app.models import db
from app.models.advisor import Advisor

def create_advisor(advisorID, lastName, firstName, initials, jobTitle, department):
    new_advisor = Advisor(
        advisorID=advisorID,
        lastName=lastName,
        firstName=firstName,
        initials=initials,
        jobTitle=jobTitle,
        department=department
    )
    db.session.add(new_advisor)
    db.session.commit()

def read_advisor(advisorID):
    return Advisor.query.filter_by(advisorID=advisorID).first()

def update_advisor(advisorID, lastName=None, firstName=None, initials=None, jobTitle=None, department=None):
    advisor = Advisor.query.filter_by(advisorID=advisorID).first()
    if lastName:
        advisor.lastName = lastName
    if firstName:
        advisor.firstName = firstName
    if initials:
        advisor.initials = initials
    if jobTitle:
        advisor.jobTitle = jobTitle
    if department:
        advisor.department = department
    db.session.commit()

def delete_advisor(advisorID):
    advisor = Advisor.query.filter_by(advisorID=advisorID).first()
    db.session.delete(advisor)
    db.session.commit()
