from datetime import datetime
from .base_model import Model
from db.database_config import DatabaseConnection

table = 'offices'
db = DatabaseConnection(  )

class Office(Model):
  """
    Class for meetup object
  """

  def __init__(self):
    super().__init__(table)

  def save(self, data):
    """
      method to add a new office
    """

    query = "INSERT INTO {} (type, name) VALUES ('{}', '{}') RETURNING *".format(
        table, data['type'], data['name']
      )

    data = db.insert(query)
    print(data)
    return data

  def office_exists(self, key, value):
    """
     method to check if a office exists
    """

    query = "SELECT * FROM {} WHERE {} = '{}'".format(
        table, key, value)

    data = db.fetch_one(query)
    return data

  def fetch_office_by_id(self, key, id):
    """
      method for fetching an office by id
    """

    query = "SELECT * FROM {} WHERE {} = '{}'".format(
        table, key, id)
            
    data = db.fetch_one(query)
    return data

  def fetch_all_offices(self):
    """
      method for fetching all political offices
    """
    query = "SELECT * FROM {}".format(table)

    data = db.fetch_all(query)
    return data

  def delete(self, office_id):
    """
      method for deleting a specific political office
    """
    query = "DELETE FROM {} WHERE id = {}".format(table, office_id)

    db.delete(query)
    return True
  

  