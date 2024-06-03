# Importing necessary modules
from flask import Flask, request, jsonify, g
from flask import Blueprint, request
from app.models import User
import bcrypt
import jwt
import datetime
import os

# Creating a Flask application instance
auth_route = Blueprint('auth', __name__)

app = Flask(__name__)

# Middleware to verify JWT token
@auth_route.before_request
def before_request():
    g.user = None
    token = request.headers.get('Authorization')
    if token:
        try:
            # Decoding and verifying JWT token
            payload = jwt.decode(token, app.config['SECRET_KEY'])
            g.user = payload['username']
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 401

# Route for user signup
@auth_route.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Checking if username and password are provided
    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    # Checking if user already exists
    user = User(username=username)
    existing_user = user.get_user_by_username()
    if existing_user is not None:
       return jsonify({'message': 'User already exists'}), 400

    # Hashing the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    print(hashed_password)

    # Creating a new user instance and saving to the database
    user.password_hash = hashed_password.decode('utf-8')
    
    user.save()

    return jsonify({'message': 'User created successfully'}), 201

# Route for user signin
@auth_route.route('/login', methods=['POST'])
def signin():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Finding user by username
    user_object = User(username=username)
    user = user_object.get_user_by_username()
    if not user:
       return jsonify({'message': 'Invalid username or password'}), 401

    print(user.keys())
    # Validating password
    if bcrypt.checkpw(password.encode('utf-8'), user["password_hash"].encode('utf-8')):
        
        # # Generating JWT token
        token = jwt.encode({'username': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, app.config['SECRET_KEY'])
    
        return jsonify({'token': token}), 200
    else:
       return jsonify({'message': 'Invalid username or password'}), 401


@auth_route.get('/users')
def get_all_users():
    users = g
    print(users.username, "users")
    return jsonify({'users': users}), 200