""" 
  Main connection to the postgres database 
"""

import sys
import os
import logging
import psycopg2
from .database_config import create_tables, destroydb, create_admin
from psycopg2.extras import RealDictCursor as dict_cursor
from instance.config import app_config

class DatabaseConnection:
  """ 
    Handles the main connection to the database of the app setting 
  """

  def __init__(self, dsn, config_name):
    """
      initialize the class instance to take a database url as a parameter
    """

    config = app_config[config_name]

    database = os.getenv('DATABASE_NAME')
    user = config.DATABASE_USERNAME
    password = config.DATABASE_PASSWORD
    host = config.DATABASE_HOST
    port = config.DATABASE_PORT

    DSN = 'dbname={} user={} password={} host={} port={}'.format(
      database, user, password, host, port
    )

    try:
      print(DSN) 
      
      self.conn = psycopg2.connect(DSN)
      self.cur = self.conn.cursor()

    except (Exception, psycopg2.DatabaseError) as error:
      print(error)

  def create_tables_and_admin(self):
    """ 
      creates all tables 
    """

    all_tables_to_create = create_tables()
    for query in all_tables_to_create:
      self.cur.execute(query)
      
    self.conn.commit()
    
  def create_admin(self):
    """ 
      create admin after creating tables
    """

    create_admin()

  def drop_all_tables(self):
    """ 
      Deletes all tables in the app 
    """

    tables_to_drop = drop_tables()
    for query in tables_to_drop:
      self.cur.execute(query)
    
    self.conn.commit

  def fetch_single_data_row(self, query):
    """ 
      retreives a single row of data from a table 
    """
    self.cur.execute(query)
    fetchedRow = cur.fetchone()
    return fetchedRow

  def save_updates(self, query):
    """ 
      saves data passed as a query to the stated table
     """
    self.cur.execute(query)
    self.conn.commit()

  def fetch_all_data(self, query):
    """ 
      fetches all data stored
    """

    self.cur.execute(query)
    all_data = cur.fetchall()
    return all_data