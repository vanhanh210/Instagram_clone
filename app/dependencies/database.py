from pymongo import MongoClient
from app.settings import DATABASE_URL, DATABASE_NAME  # Importing centralized configurations

# Ensure the client is initialized only once
if 'client' not in locals():
    client = MongoClient(DATABASE_URL)  # Using the centralized connection string

db = client[DATABASE_NAME]  # Using the centralized database name

# Define collections
users_collection = db["users"]
posts_collection = db["posts"]
comments_collection = db["comments"]
