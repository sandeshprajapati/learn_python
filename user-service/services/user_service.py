# services/user_service.py
from repositories.user_repository import UserRepository

class UserService:
    @staticmethod
    def create_user(username, email):
        user = UserRepository.create_user(username, email)
        return user.to_dict()

    @staticmethod
    def get_user(user_id):
        user = UserRepository.get_user_by_id(user_id)
        if user:
            return user.to_dict()
        return None

    @staticmethod
    def update_user(user_id, username, email):
        user = UserRepository.update_user(user_id, username, email)
        if user:
            return user.to_dict()
        return None

    @staticmethod
    def delete_user(user_id):
        if UserRepository.delete_user(user_id):
            return {"message": "User deleted successfully"}
        return {"error": "User not found"}

    @staticmethod
    def get_all_users():
        users = UserRepository.get_all_users()
        return [user.to_dict() for user in users]
