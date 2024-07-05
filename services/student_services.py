from app.models import db
from app.models.student import Student

def create_student(studentID, lastName, firstName, initials, major, advisorID):
    new_student = Student(
        studentID=studentID,
        lastName=lastName,
        firstName=firstName,
        initials=initials,
        major=major,
        advisorID=advisorID
    )
    db.session.add(new_student)
    db.session.commit()

def read_student(studentID):
    return Student.query.filter_by(studentID=studentID).first()

def update_student(studentID, lastName=None, firstName=None, initials=None, major=None, advisorID=None):
    student = Student.query.filter_by(studentID=studentID).first()
    if lastName:
        student.lastName = lastName
    if firstName:
        student.firstName = firstName
    if initials:
        student.initials = initials
    if major:
        student.major = major
    if advisorID:
        student.advisorID = advisorID
    db.session.commit()

def delete_student(studentID):
    student = Student.query.filter_by(studentID=studentID).first()
    db.session.delete(student)
    db.session.commit()
