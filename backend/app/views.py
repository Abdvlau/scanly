# Import necessary modules from flask
from flask import Blueprint, jsonify

# Create a new Blueprint object
main_blueprint = Blueprint('main', __name__)

# Define a route for the root URL ("/")
@main_blueprint.route('/')
# Define the function to be called when the root URL is accessed
def home():
    # Return a JSON response with a welcome message
    return jsonify({'message': 'Welcome to the Scanly API!🔥🔥🔥'})