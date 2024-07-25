# app/models/__init__.py

from flask_sqlalchemy import SQLAlchemy

# Define db object without initializing it
db = SQLAlchemy()

# Import models after db is initialized
from .advisor import Advisor
from .user import User
from .department import Department
from .course import Course
from .grade import Grade
# other models ...
