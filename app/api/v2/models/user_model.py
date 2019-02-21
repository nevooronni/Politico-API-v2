from datetime import datetime
import json
from werkzeug.security import generate_password_hash, check_password_hash
from db.database_config import DatabaseConnection

table = 'users'
db = DatabaseConnection()

class User(object):
  """
    Model class for user object
  """

  def save(self, data):
    """
      method to save new user
    """

    othername = 'othername'
    passporturl = 'passporturl'

    def set_field_value(data, value):
      """
        sets value for not required fields
      """

      if value in data:
        return data[value]
      else:
        return None   

    password = generate_password_hash(data['password'])
    data['isAdmin'] = False
    data['isPolitician'] = False
 
    query = "INSERT INTO {} (firstname, lastname, othername, phonenumber, email, password, passporturl, isAdmin, isPolitician) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}','{}') RETURNING *".format(
        table, data['firstname'], 
        data['lastname'], set_field_value(data, othername), data['phonenumber'], data['email'], password, set_field_value(data, passporturl), data['isAdmin'], data['isPolitician']
      )

    data = db.insert(query)
    print(data)
    return data

  def get_all_users(self):
    """
      Fetch all users
    """
    query = "SELECT * FROM {}".format(table)
    users = db.fetch_all(query)
    return json.dumps(users, default=str)
    
  def user_exists(self, key, value):
    """
     method to check if a user exists
    """
    query = "SELECT * FROM {} WHERE {} = '{}'".format(
        table, key, value)

    data = db.fetch_one(query)
    return data

    return data

  def find_user_by_phonenumber(self, key, phonenumber):
    """
      method to find a user by username
    """
    # got_user = [user for user in users if user['phoneNumber'] == phoneNumber]
    # return got_user[0]

    query = "SELECT * FROM {} WHERE {} = '{}'".format(
        table, key, phonenumber)
            
    data = db.fetch_one(query)
    return data

  def check_password(self, hash, password):
    """
      method to check if the passwords match
    """

    return check_password_hash(hash, password)

