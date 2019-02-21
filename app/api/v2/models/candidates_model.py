from datetime import datetime
from .base_model import Model
from db.database_config import DatabaseConnection

table = 'candidates'
db = DatabaseConnection(  )

class Candidate(Model):
  """
    Class for candidate object
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

  def fetch_all_candidates(self):
    """
      method for fetching all candidates
    """
    query = "SELECT * FROM {}".format(table)

    data = db.fetch_all(query)
    return data

  def check_if_it_exists_for_specific_office(self, key, value, office_id):
    """
      method to check if a candidates exists in a specific office
    """
    specific_office_candidates = []
    all_candidates = self.fetch_all_candidates()
    for candidate in all_candidates:
      if (candidate['office'] == office_id):
        specific_office_candidates.append(candidate)
        print(specific_office_candidates)
        if candidate[key] == value:
          return candidate
        else:
          return False