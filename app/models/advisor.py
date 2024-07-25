from . import db

class Advisor(db.Model):
    advisorID = db.Column(db.String(6), primary_key=True)
    lastName = db.Column(db.String(50))
    firstName = db.Column(db.String(50))
    initials = db.Column(db.String(3))
    jobTitle = db.Column(db.String(128))
    department = db.Column(db.String(50))
