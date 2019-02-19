from flask import jsonify, request, abort, make_response
from flask.views import MethodView
from ..schemas.user_schema import UserSchema
# from ..models.user_model import User
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required,get_jwt_identity, jwt_refresh_token_required, get_raw_jwt)

# db = User()

class IndexAPI(MethodView):
  """
    class for index route endpoint
  """

  def get(self):
    return jsonify({
      'status': 200,
      'message': 'welcome to Politico API Web service, use the base url: https://politco-api.herokuapp.com/api/v1 for posting your requests'
    })


index_view = IndexAPI.as_view('index_api') 
