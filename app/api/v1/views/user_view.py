from flask import jsonify, request, abort, make_response
from ...v1 import version_1 as v1
from ..schemas.user_schema import UserSchema
from ..models.user_model import User
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required,get_jwt_identity, jwt_refresh_token_required, get_raw_jwt)

db = User()

@v1.route('/', methods=['GET'])
@v1.route('/index', methods=['GET'])
def index():
    return jsonify({
      'status': 200, 
      'message': 'Welcome to Questioner API web service!'
    }), 200