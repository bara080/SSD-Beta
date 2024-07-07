from app import db

class Student(db.Model):
    studentID = db.Column(db.String(9), primary_key=True)
    lastName = db.Column(db.String(50), nullable=False)
    firstName = db.Column(db.String(50), nullable=False)
    initials = db.Column(db.String(3))
    dateOfBirth = db.Column(db.Date)
    gender = db.Column(db.String(1))
    email = db.Column(db.String(100))
    address = db.Column(db.String(255))
    city = db.Column(db.String(100))
    state = db.Column(db.String(50))
    zipCode = db.Column(db.String(20))
    phone = db.Column(db.String(20))
    major = db.Column(db.String(128))
    advisorID = db.Column(db.String(6), db.ForeignKey('advisor.advisorID'), nullable=True)
