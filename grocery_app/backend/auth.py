from flask import Blueprint, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from sql_connection import get_sql_connection
from flask_cors import cross_origin
from flask import jsonify, session
auth_bp = Blueprint('auth', __name__)
connection = get_sql_connection()

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data['username']
    password = generate_password_hash(data['password'])

    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        connection.commit()
        return jsonify({"message": "User registered successfully"}), 201
    except:
        return jsonify({"message": "Username already exists"}), 409

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    print(username)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    print(user)
    if user and check_password_hash(user[2], password):
        session['user_id'] = user[0]
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

@auth_bp.route('/logout', methods=['POST'])
@cross_origin(origin='http://localhost:63342', supports_credentials=True)
def logout():
    session.clear()
    return jsonify({"message": "Logged out successfully"}), 200