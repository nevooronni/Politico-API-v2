"""create app"""

import os
from flask import Flask 
from instance.config import app_config


def create_app(config_name):
  """
    Create app using specified environment configurations
  """

  app = Flask(__name__, instance_relative_config=True)
  app.config.from_object(app_config[config_name])
  app.config.from_pyfile('config.py')
  app.secret_key = os.getenv('SECRET_KEY')


  print("lastchance is up and running!")
  return app
