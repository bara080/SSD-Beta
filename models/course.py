from . import db

class Course(db.Model):
    coursePrefix = db.Column(db.String(9), primary_key=True)
    courseName = db.Column(db.String(50))
    creditHours = db.Column(db.Integer)
