# controllers/user_controller.py
from flask import Blueprint, request, jsonify
from services.user_service import UserService

user_controller = Blueprint('user_controller', __name__)

@user_controller.route('/users', methods=['GET'])
def get_all_users():
    users = UserService.get_all_users()
    return jsonify(users), 200

@user_controller.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = UserService.get_user(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

@user_controller.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    if not username or not email:
        return jsonify({"error": "Username and email are required"}), 400
    user = UserService.create_user(username, email)
    return jsonify(user), 201

@user_controller.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    if not username or not email:
        return jsonify({"error": "Username and email are required"}), 400
    user = UserService.update_user(user_id, username, email)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

@user_controller.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    result = UserService.delete_user(user_id)
    if result:
        return jsonify(result), 200
    return jsonify({"error": "User not found"}), 404
