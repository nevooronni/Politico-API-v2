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
      method for fetching all votes
    """
    
    query = "SELECT * FROM {}".format(table)

    data = db.fetch_all(query)
    return data

  def fetch_results(self, office_id):
    """
      method for fetching all results for a particular office
    """

    all_votes = self.fetch_all_votes()
    specific_office_votes = []
    all_votes = self.fetch_all_votes()
    print(all_votes)
    for vote in all_votes:
      if (vote['office'] == office_id):
        specific_office_votes.insert(len(specific_office_votes), vote)
        return specific_office_votes
      else:
        None

  
  def check_if_vote_exists_for_specific_office(self, key, value, value2):
    """
      method to check if a candidates exists in a specific office
    """
    specific_office_votes = []
    all_votes = self.fetch_all_votes()
    for vote in all_votes:
      if (vote['office'] == value2):
        specific_office_votes.append(vote)
        print(specific_office_votes)
        if vote[key] == value:
          return vote
        else:
          return False
  
