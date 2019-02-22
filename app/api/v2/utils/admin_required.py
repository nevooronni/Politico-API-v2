
from flask_jwt_extended import get_jwt_identity
from functools import wraps
import json
from flask import jsonify
from app.api.v2.models.user_model import User


def admin_required(func):
    """
      Helper method to limit access rights to specific endpoints
    """
    @wraps(func)
    def wrapper_function(*args, **kwargs):
        users = User().get_all_users()
        users = json.loads(users)
        try:
            cur_user = [
                user for user in users if user['id'] == get_jwt_identity()]
            user_role = cur_user[0]['isadmin']
            if user_role != True:
                return jsonify({
                    'message': 'Forbidden only admin users have access to this endpoint'}), 403 # Forbidden
            return func(*args, **kwargs)
        except Exception as e:
            return jsonify({"message": str(e)}),500
    return wrapper_function