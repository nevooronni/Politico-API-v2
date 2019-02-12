"""create app"""

import os
from flask import Flask
from instance.config import app_config
from flask_jwt_extended import (JWTManager)
from app.api.v1.models.token_model import RevokedTokenModel
# from app.api.v1.views.user_view import v1 as users_blueprint
# from app.api.v1.views.party_view import v1 as parties_blueprint
# from app.api.v1.views.office_view import v1 as offices_blueprint
from app.api.v1.views.user_view import index_view, signup_auth_view, signin_auth_view, token_view

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
    from app.api.v1.models.token_model import RevokedTokenModel
    jti = token['jti']
    return RevokedTokenModel().is_blacklisted(jti)

  #register blueprint
  # app.register_blueprint(users_blueprint)
  # app.register_blueprint(parties_blueprint)
  # app.register_blueprint(offices_blueprint)
  app.add_url_rule('/api/v1/index', view_func=index_view, methods=['GET'])
  app.add_url_rule('/api/v1/signup', view_func=signup_auth_view, methods=['POST'])
  app.add_url_rule('/api/v1/refresh-token', view_func=token_view, methods=['POST'])
  app.add_url_rule('/api/v1/signin', view_func=signin_auth_view, methods=['POST'])

  return app
