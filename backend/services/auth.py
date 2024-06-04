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


config_class = get_config()
app.config['SECRET_KEY'] = "kalifa"
#app.config.from_object(config_class)

# Middleware to verify JWT token
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        # Check if the token is in the request headers
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]  # Assuming 'Bearer <token>'
        
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        
        try:
            # Decode the token
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = data['username']
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token!'}), 401
        
        return f(current_user, *args, **kwargs)
    
    return decorated

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
    user.enrollment_id = data.get('enrollment_id')
    
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


@auth_route.route('/protected', methods=['GET'])
@token_required
def protected_route(current_user):
    return jsonify({'username': current_user})