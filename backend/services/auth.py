# Importing necessary modules
from flask import Flask, request, jsonify, g
from flask import Blueprint, request
from app.models import User
import bcrypt
import jwt
import datetime
from functools import wraps
import os
from config import get_config

# Creating a Flask application instance
auth_route = Blueprint('auth', __name__)

app = Flask(__name__)

# Get the configuration class
config_class = get_config()

# Set the secret key for the Flask application
app.config['SECRET_KEY'] = "kalifa"

# Middleware to verify JWT token
def token_required(f):
    # This function will be used as a decorator to secure routes
    # It checks if a valid JWT token is present in the request
    @wraps(f)
    def decorated(*args, **kwargs):
        # Get the token from the request headers
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        # If there's no token, return an error
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            # Try to decode the token
            data = jwt.decode(token, app.config['SECRET_KEY'])
            # Get the user from the database
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            # If the token is invalid, return an error
            return jsonify({'message': 'Token is invalid!'}), 401

        # If the token is valid, call the decorated function and pass the user as an argument
        return f(current_user, *args, **kwargs)

    return decorated