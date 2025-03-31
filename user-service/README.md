# learn_python
# User Service

The `user-service` is a Flask-based RESTful API for managing user data. It provides endpoints for creating, reading, updating, and deleting user records.

## Features

- Create a new user
- Retrieve a user by ID
- Update user details
- Delete a user
- List all users

## Project Structure


## Prerequisites

- Python 3.8+
- MySQL database
- Flask and required dependencies (see `requirements.txt`)

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd learn_python/user-service
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt  
   ``` 
3. Configure the database:
   Update the SQLALCHEMY_DATABASE_URI in config.py with your MySQL credentials.
4. Run the application:
   ```bash 
   flask run
   ```
5. Access the API at http://127.0.0.1:5000.

## API Endpoints
Users
GET /users
Retrieve all users.

GET /users/<user_id>
Retrieve a user by ID.

POST /users
Create a new user.
Request Body:

```bash
{
  "username": "example",
  "email": "example@example.com"
}
```
PUT /users/<user_id>
Update an existing user.
Request Body:
```bash
{
  "username": "new_username",
  "email": "new_email@example.com"
}
```
DELETE /users/<user_id>
Delete a user by ID.

