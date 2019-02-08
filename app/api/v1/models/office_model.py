from datetime import datetime
from ..utils.utils import generate_id
from .base_model import Model

offices = []

class Office(Model):
  """
    Class for meetup object
  """

  def __init__(self):
    super().__init__(offices)

  def save(self, data):
    """
      method to add a new office
    """

    data['id'] = generate_id(self.collection)
    return super().save(data)

  def office_exists(self, key, value):
    """
     method to check if a office exists
    """

    got_office = [office for office in offices if value == office[key]]
    return len(got_office) > 0

  def fetch_office_by_id(self, id):
    """
      method for fetching an office by id
    """

    offices_fetched = [office for office in offices if office['id'] == id]
    return offices_fetched[0]

  def fetch_all_offices(self):
    """
      method for fetching all political offices
    """
    return offices

  # def update_party(self, party_id, name):
  #   """ 
  #     method to update a party's name
  #   """

  #   for party in political_parties:
  #     if party['id'] == party_id:
  #       party['name'] = name

  #     return party

  

  