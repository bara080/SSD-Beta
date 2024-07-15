import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

#  Generate 24 unique random secret key
os.urandom(24)
class Config:
    # Database configuration
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DB_NAME = os.getenv('DB_NAME')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')


    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
