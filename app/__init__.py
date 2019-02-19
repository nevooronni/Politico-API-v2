"""create app"""

import os
from flask import Flask, Blueprint, make_response, jsonify
from instance.config import app_config
from flask_jwt_extended import (JWTManager)
from app.api.v2.models.token_model import RevokedTokenModel
# from app.api.v1.views.user_view import v1 as users_blueprint
# from app.api.v1.views.party_view import v1 as parties_blueprint
# from app.api.v1.views.office_view import v1 as offices_blueprint
from app.api.v2.views.user_view import index_view, signup_auth_view, token_view
# from app.api.v2.views.party_view import create_party_view, fetch_party_view, fetch_all_parties_view, update_party_view,delete_party_view
# from app.api.v2.views.office_view import create_office_view, fetch_office_view, fetch_all_offices_view, delete_office_view
from db.database_config import DatabaseConnection
# from app.api.v2.views.user_view import index_view

def page_not_found(e):
  """
    function that handles 404 error
  """

  return make_response(jsonify({
    "status": 404,
    "message": "url does not exist"
  }), 404)


def method_not_allowed(e):
  """
    function that handles 405 error
  """

  return make_response(jsonify({
    "status": 405,
    "message": "method not allowed"
  }), 405)


def initialize_database(config_name):
    """method for initializing the db """

    print(config_name)
    try:
      db = DatabaseConnection()
      db.init_connection(config_name)
      db.drop_tables()
      db.create_tables()
      db.create_admin()

    except Exception as error:
        print('Error initiating DB: {}'.format(str(error)))


def create_app(config_name):
  """
    Create app using specified environment configurations
  """

  app = Flask(__name__, instance_relative_config=True)
  app.config.from_object(app_config[config_name])
  app.config.from_pyfile('config.py')
  app.secret_key = os.getenv('SECRET_KEY')
  
  #Initialize JWT
  jwt = JWTManager(app)
  @jwt.token_in_blacklist_loader
  def check_blacklisted(token):
    from app.api.v2.models.token_model import RevokedTokenModel
    jti = token['jti']
    return RevokedTokenModel().is_blacklisted(jti)

  #Initialize database
  initialize_database(config_name)

  #register blueprint
  # app.register_blueprint(users_blueprint)
  # app.register_blueprint(parties_blueprint)
  # app.register_blueprint(offices_blueprint)
  app.register_error_handler(404, page_not_found)
  app.register_error_handler(405, method_not_allowed)


  #v1 method view routes
  app.add_url_rule('/api/v2/index', view_func=index_view, methods=['GET'])
  app.add_url_rule('/api/v2/auth/signup', view_func=signup_auth_view, methods=['POST'])
  app.add_url_rule('/api/v2/auth/refresh-token', view_func=token_view, methods=['POST'])
  # app.add_url_rule('/api/v1/signin', view_func=signin_auth_view, methods=['POST'])
  # app.add_url_rule('/api/v1/parties', view_func=create_party_view, methods=['POST'])
  # app.add_url_rule('/api/v1/parties/<int:party_id>', view_func=fetch_party_view, methods=['GET'])
  # app.add_url_rule('/api/v1/parties', view_func=fetch_all_parties_view, methods=['GET'])
  # app.add_url_rule('/api/v1/parties/<int:party_id>/name', view_func=update_party_view, methods=['PATCH'])
  # app.add_url_rule('/api/v1/parties/<int:party_id>', view_func=delete_party_view, methods=['DELETE'])
  # app.add_url_rule('/api/v1/offices', view_func=create_office_view, methods=['POST'])
  # app.add_url_rule('/api/v1/offices/<int:office_id>', view_func=fetch_office_view, methods=['GET'])
  # app.add_url_rule('/api/v1/offices', view_func=fetch_all_offices_view, methods=['GET'])
  # app.add_url_rule('/api/v1/offices/<int:office_id>', view_func=delete_office_view, methods=['DELETE'])

  # #v2 method view routes
  # app.add_url_rule('/api/v2/index', view_func=index_view, methods=['GET'])


  return app

