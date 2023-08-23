# Instagram_clone

This is a basic RESTful API for an Instagram clone, built using FastAPI and MongoDB. The API allows users to sign up, log in, create posts, and add comments to posts.

# Features
- User authentication with JWT tokens.
- CRUD operations for posts.
- CRUD operations for comments.
- File upload for post images.
# Requirements
- Python 3.8+
- MongoDB
- fastapi
- beanie
- uvicorn
- motor
- passlib
- pydantic[email]
- jose[3.3.0]
- python-multipart
# Instalation

**1. Clone the repository:**
```
git clone https://github.com/yourusername/instagram-clone.git
```
**2. Navigate to the project directory:**
```
cd instagram-clone
```
**3. Install the required packages:**
```
pip install -r requirements.txt
```
# Running the API
```
uvicorn app.main:app --reload
```
# Database Setup
- Define MongoDB collections for users, posts, and comments.
- Initialize database connections.
```
DATABASE_URL = "mongodb://localhost:27017"  # Update if your MongoDB is hosted elsewhere
DATABASE_NAME = "instagram"
```
# Endpoints
- `POST /signup:` Sign up a new user.
- `POST /login:` Authenticate and retrieve an access token.
- `POST /create-post:` Create a new post.
- `GET /list-posts:` Retrieve a list of all posts and their associated comments.
- `POST /create-comment:` Add a comment to a post.
- `GET /get-comments/{post_id}:` Retrieve all comments for a specific post.

# Structure
```
 Instagram_clone 
	app/
		dependencies/
			__init__.py
			database.py
			security.py
		models
			comment.py
			post.py
			user.py
		routers
			comments.py
			posts.py
			authentication.py
	main.py
	setting.py
	requirements.py	
```
# Resource
- https://fastapi.tiangolo.com
- https://beanie-odm.dev/
- https://www.mongodb.com
- https://www.ibm.com/topics/rest-apis
- https://viblo.asia/p/tich-hop-fastapi-voi-authentication-bang-jwt-XL6lA6rR5ek


