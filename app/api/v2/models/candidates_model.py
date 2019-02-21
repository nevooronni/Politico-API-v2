from datetime import datetime
from .base_model import Model
from db.database_config import DatabaseConnection

table = 'candidates'
db = DatabaseConnection(  )

class Candidate(Model):
  """
    Class for meetup object
  """

  def __init__(self):
    super().__init__(table)

  def save(self, data):
    """
      method to add a new candidate
    """

    query = "INSERT INTO {} (office, user_id) VALUES ('{}', '{}') RETURNING *".format(
        table, data['office_id'], data['user_id']
      )

    data = db.insert(query)
    print(data)
    return data

  def candidate_exists(self, key, value):
    """
     method to check if a candidate exists
    """

    query = "SELECT * FROM {} WHERE {} = '{}'".format(
        table, key, value)

    data = db.fetch_one(query)
    return data
  
