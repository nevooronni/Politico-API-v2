import psycopg2
# import instance.config import app_config
from werkzeug.security import generate_password_hash

# host = 'localhost'
# user = 'nevooronni'
# port = 5000
# password = 'speeds01'
# dbname = 'myblog'
# connection_url = "dbname='myblog' host='127.0.0.1' port='5000' user='nevooronni' password='speeds01'"

# config = app_config[config_name]

# database = os.getenv('DATABASE_NAME')
# user = config.DATABASE_USERNAME
# password = config.DATABASE_PASSWORD
# host = config.DATABASE_HOST
# port = config.DATABASE_PORT

# DSN = 'dbname={} user={} password={} host={} port={}'.format(
#   database, user, password, host, port
# )

# uri = DSN
#return connections
def connection(uri):
  con = psycopg2.connect(uri)
  return con

#returns connection and creates tables
def init_db(uri):
  con = connection(uri)
  cur = con.cursor()
  queries = tables()

  for query in queries:
    cur.execute(query)
  con.commit()

  return con

#returns connection and creates tables (TDD)
def init_test_db(test_uri):
  con = connection(test_uri)
  cur = con.cursor()
  queries = tables()

  for query in queries:
    cur.execute(query)
  con.commit()

  return con

#destroys all tables after tests have been ran
def destroydb():
  con = connection(test_uri)
  cur = con.cursor()
  users = """ DROP TABLE IF EXISTS users CASCADE; """
  parties = """ DROP TABLE IF EXISTS parties CASCADE; """
  offices = """ DROP TABLE IF EXISTS offices CASCADE; """
  queries = [users, parties, offices]

  for query in queries:
    cur.execute(query)
  con.commit()

#contains all talbes creation queiries
def create_tables():
  users = """ CREATE TABLE IF NOT EXISTS users (
    user_id serial PRIMARY KEY NOT NULL,
    firstname character varying(50) NOT NULL,
    lastname character varying(50) NOT NULL,
    othername character varying(50),
    password character varying(50) NOT NULL,
    phoneNumber integer NOT NULL,
    email character varying(50) NOT NULL,
    passportUrl character varying(50), 
    isAdmin boolean
  ); """

  parties = """ CREATE TABLE IF NOT EXISTS parties (
    id serial PRIMARY KEY NOT NULL,
    name character varying(50) NOT NULL,
    hqAddress character varying(50) NOT NULL, 
    logoUrl character varying(50)
  ); """

  offices = """ CREATE TABLE IF NOT EXISTS offices (
    id serial PRIMARY KEY NOT NULL,
    type character varying(50) NOT NULL,
    name character varying(50) NOT NULL 
  ); """

  queries = [users, parties, offices]
  return queries

def drop_tables():
  """
    function for drop database tables
  """

  drop_users = """ DROP TABLE IF EXISTS users """
  drop_parties = """ DROP TABLE IF EXISTS parties """
  drop_offices = """ DROP TABLE IF EXISTS offices """

  return [drop_books, drop_users]

def create_admin(conn):
  """ 
    Function to insert super admin into the db 
  """

  user_query = "SELECT * FROM users WHERE username = 'nevooronni'"
  cur.execute(user_query)
  result = cur.fetchone()

  if not result:
    cur = conn.cursor()
    cur.execute("INSERT INTO users (firstname, lastname, username, phoneNumber, email,\
      password, admin) VALUES ('Neville', 'Oronni', 'Gerald', '0712345678',\
      'nevooronni@gmail.com', '{}', True)\
      ".format(generate_password_hash('abc1$#De0')))

    conn.commit()

  