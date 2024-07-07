from . import db
class Grade(db.Model):
    gradeID = db.Column(db.Integer, primary_key=True)
    studentID = db.Column(db.String(9), db.ForeignKey('student.studentID'))
    coursePrefix = db.Column(db.String(9), db.ForeignKey('course.coursePrefix'))
    semester = db.Column(db.String(6))
    grade = db.Column(db.Numeric(5, 2))