from . import db

class Department(db.Model):
    departmentID = db.Column(db.String(6), primary_key=True)
    departmentName = db.Column(db.String(50))
