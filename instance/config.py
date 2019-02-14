"""App configurations"""

import os

class Config(object):
  """
    Parent configuration class.
  """
  
  DEBUG = False
  TESTING = False
  DATABASE_HOST = os.getenv('DATABASE_HOST')
  DATABASE_PORT = os.getenv('DATABASE_PORT')
  DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
  DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
  JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
  SECRET_KEY = os.getenv('SECRET_KEY')
  JWT_BLACKLIST_ENABLED = True
  JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']

class DevelopmentConfig(Config):
  """
    Configurations for Development.
  """
  DEBUG = True
  DATABASE_DSN = os.getenv("DEV_DB_DSN")

class TestingConfig(Config):
  """
    Configuration for Testing with a seperate test database.
  """

  TESTING = True
  DEBUG = True
  DATABASE_DSN = os.getenv("TESTING_DB_DSN")



class StagingConfig(Config):
  """
    Configuration for Staging
  """
  DEBUG = True
  DATABASE_DSN = os.getenv("STAGING_DB_DSN")



class ProductionConfig(Config):
  """
    Configuration for Production
  """

  DEBUG = False
  TESTING = False
  DATABASE_DSN = os.getenv("PRODUCTION_DB_DSN")



app_config = {
  'development': DevelopmentConfig,
  'testing': TestingConfig,
  'staging': StagingConfig,
  'production': ProductionConfig,
}
