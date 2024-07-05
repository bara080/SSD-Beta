# from flask_login import UserMixin
# from app import mongo

# class Advisor(UserMixin):
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password

#     @staticmethod
#     def get_by_username(username):
#         return mongo.db.advisors.find_one({"username": username})

#     @staticmethod
#     def create(username, password):
#         mongo.db.advisors.insert_one({
#             "username": username,
#             "password": password
#         })

# class Student(UserMixin):
#     def __init__(self, username, password, department, schedule):
#         self.username = username
#         self.password = password
#         self.department = department
#         self.schedule = schedule

#     @staticmethod
#     def get_by_username(username):
#         return mongo.db.students.find_one({"username": username})

#     @staticmethod
#     def create(username, password, department):
#         mongo.db.students.insert_one({
#             "username": username,
#             "password": password,
#             "department": department,
#             "schedule": []
#         })

# class Department:
#     @staticmethod
#     def create(name, professors, classes):
#         mongo.db.departments.insert_one({
#             "name": name,
#             "professors": professors,
#             "classes": classes
#         })

#     @staticmethod
#     def get_all():
#         return list(mongo.db.departments.find())

#     @staticmethod
#     def get_by_name(name):
#         return mongo.db.departments.find_one({"name": name})
from . import db

class Grade(db.Model):
    gradeID = db.Column(db.Integer, primary_key=True)
    studentID = db.Column(db.String(9), db.ForeignKey('student.studentID'))
    coursePrefix = db.Column(db.String(9), db.ForeignKey('course.coursePrefix'))
    semester = db.Column(db.String(6))
    grade = db.Column(db.Numeric(5, 2))
