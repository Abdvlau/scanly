# Import the User model from the app.models module
from app.models import User

# Define a function to create a new user
def create_user(username, email):
    # Create a new User object with the given username and email
    user = User(username=username, email=email)
    # Save the user to the database
    user.save()

# Define a function to get a user by username
def get_user(username):
    # Query the database for a user with the given username
    user = User.objects(username=username).first()
    # Return the user
    return user

# Define a function to get all users
def get_all_users():
    # Query the database for all users
    users = User.objects()
    # Return the users
    return users