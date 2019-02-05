"""create app"""

import os
from flask import Flask 
from instance.config import app_config
from app.api.v1.views.user_view import v1 as users_blueprint

def create_app(config_name):
  """
    Create app using specified environment configurations
  """

  app = Flask(__name__, instance_relative_config=True)
  app.config.from_object(app_config[config_name])
  app.config.from_pyfile('config.py')
  app.secret_key = os.getenv('SECRET_KEY')

  #register blueprint
  app.register_blueprint(users_blueprint)

  return app
