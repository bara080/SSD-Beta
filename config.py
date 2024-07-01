import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# config = dotenv_values(".env")
def mongo_connectdb():
    # Retrieve the MongoDB URI from the environment variable
    mongo_uri = os.getenv("MONGODB_URI")

    if not mongo_uri:
        raise ValueError("No MONGODB_URI set for the database connection")

    try:
        # Establishing the connection
        client = MongoClient(mongo_uri)
        db = client.get_default_database("piedb")
        print("MongoDB connection established successfully.")
        return db
    except Exception as e:
        print(f"Unable to connect to MongoDB: {e}")
        return None
    

