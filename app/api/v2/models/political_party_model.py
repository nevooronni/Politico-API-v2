from datetime import datetime
from .base_model import Model
from db.database_config import DatabaseConnection

table = 'parties'
db = DatabaseConnection()

class PoliticalParty(Model):
  """
    Class for political party object
  """

  def __init__(self):
    super().__init__(table)

  def save(self, data):
    """
      method to add a new meetup
    """

    hqaddress = 'hqaddress'
    logourl = 'logourl'

    def set_field_value(data, value):
      """
        sets value for not required fields
      """

      if value in data:
        return data[value]
      else:
        return None   

    query = "INSERT INTO {} (name, hqaddress, logourl) VALUES ('{}', '{}', '{}') RETURNING *".format(
        table, data['name'], 
        set_field_value(data, hqaddress), set_field_value(data, logourl)
      )

    data = db.insert(query)
    print(data)
    return data

  def party_exists(self, key, value):
    """
     method to check if a party exists
    """
    query = "SELECT * FROM {} WHERE {} = '{}'".format(
        table, key, value)

    data = db.fetch_one(query)
    return data

  def fetch_party_by_id(self, key, id):
    """
      method for fetching a party by id
    """

    query = "SELECT * FROM {} WHERE {} = '{}'".format(
        table, key, id)
            
    data = db.fetch_one(query)
    return data

  def fetch_all_parties(self):
    """
      method for fetching all political parties
    """
    query = "SELECT * FROM {}".format(table)

    data = db.fetch_all(query)
    return data

  def update_party(self, party_id, name):
    """ 
      method to update a party's name
    """

    party = self.fetch_party_by_id('id', party_id)
    party['name'] = name

    query = "UPDATE {} SET name = '{}' WHERE id = '{}' \
    RETURNING *".format(table, name, party_id)

    return db.insert(query)

  def delete(self, party_id):
    """
      method for deleting a political party 
    """
    query = "DELETE FROM {} WHERE id = {}".format(table, party_id)

    db.delete(query)
    return True


  

  