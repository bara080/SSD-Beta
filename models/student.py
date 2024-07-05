from . import db

class Student(db.Model):
    studentID = db.Column(db.String(9), primary_key=True)
    lastName = db.Column(db.String(50))
    firstName = db.Column(db.String(50))
    initials = db.Column(db.String(3))
    major = db.Column(db.String(128))
    advisorID = db.Column(db.String(6), db.ForeignKey('advisor.advisorID'))
