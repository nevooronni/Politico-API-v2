import sys
import logging
import psycopg2
from instance.config import app_config
from db.database_tables import tables, create_table_queries
from werkzeug.security import generate_password_hash
from psycopg2.extras import RealDictCursor


class DatabaseConnection:

  def init_connection(self, config_name):
    """ 
      method to initialize db connection
    """

    config = app_config[config_name]

    # database = config.DATABASE_NAME
    # user = config.DATABASE_USERNAME
    # password = config.DATABASE_PASSWORD
    # host = config.DATABASE_HOST
    # port = config.DATABASE_PORT

    database = config.DATABASE_URL
    DSN = database

    try:
      global conn, cur

      conn = psycopg2.connect(DSN)
      cur = conn.cursor(cursor_factory=RealDictCursor)

    except Exception as error:
      print('Error. Unable to establish Database connection')

      logger = logging.getLogger('database')
      logger.error(str(error))

      sys.exit(1)


  def create_tables(self):
    """ 
      method to create tables 
    """

    for query in create_table_queries:
      cur.execute(query)

    conn.commit()

  def create_admin(self):
    """ 
      method to insert an admin user into the db 
    """

    user_query = "SELECT * FROM users WHERE firstname = 'Neville'"
    cur.execute(user_query)
    result = cur.fetchone()

    if not result:
      cur.execute("INSERT INTO users (firstname, lastname, othername, phoneNumber, email,\
      password, isAdmin, isPolitician) VALUES ('Neville', 'Oronni', 'Gerald', '0712345678',\
      'nevooronni@gmail.com', '{}', True, False)\
        ".format(generate_password_hash('asf8$#Er0')))
      conn.commit()

  def insert(self, query):
    """ 
      method to insert new item into the db 
    """
    cur.execute(query)
    data = cur.fetchone()
    conn.commit()
    return data

  def fetch_one(self, query):
    """ 
      method to fetch one item from the db 
    """
    cur.execute(query)
    data = cur.fetchone()
    return data

  def fetch_all(self, query):
    """ 
      method to fetch all items from the db 
    """
    cur.execute(query)
    data = cur.fetchall()
    return data

  def delete(self, query):
    """ 
      method to remove item from the db 
    """
    cur.execute(query)
    conn.commit()

  def drop_tables(self):
    """ 
      method to drop tables 
    """

    for table in tables:
      cur.execute('DROP TABLE IF EXISTS {} CASCADE'.format(table))

      conn.commit()

  