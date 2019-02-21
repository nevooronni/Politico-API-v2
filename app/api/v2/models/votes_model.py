from datetime import datetime
from .base_model import Model
from db.database_config import DatabaseConnection

table = 'votes'
db = DatabaseConnection(  )

class Votes(Model):
  """
    Class for votes object
  """

  def __init__(self):
    super().__init__(table)

  def save(self, data):
    """
      method to add a new candidate
    """

    query = "INSERT INTO {} (voter, office, candidate) VALUES ('{}', '{}', '{}') RETURNING *".format(
        table, data['voter'], data['office'], data['candidate']
      )

    data = db.insert(query)
    print(data)
    return data

  def vote_exists(self, key, value):
    """
     method to check if a vote from specific user exists
    """

    query = "SELECT * FROM {} WHERE {} = '{}'".format(
        table, key, value)

    data = db.fetch_one(query)
    return data

  def fetch_all_votes(self):
    """
      method for fetching all political offices
    """
    query = "SELECT * FROM {}".format(table)

    data = db.fetch_all(query)
    return data
  
