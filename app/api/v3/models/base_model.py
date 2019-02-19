from datetime import datetime
from ....database_config import init_db

class BaseModel(object):
  """
    Base model class
  """

  def __init__(self, collection):
    """
      initializes list of an object type
    """
    self.collection = collection

  def save(self, data):
    """
      method to save object
    """
    data['createdOn'] = datetime.now()
    self.collection.append(data)
    return data

  def check_if_it_exists(self, table_name, field_name, value):
    """
      method to check if an object exist using key, value pair
    """
    con = init_db()
    cur = con.cursor()
    query = "SELECT * FROM {} WHERE {}='{}';".format(table_name, field_name, value)
    cur.execute(query)
    resp = cur.fetchall()
    if resp:
      return True
    else:
      return False

  # def find(self, key, value):
  #   """
  #     method to find object item using key, value pair
  #   """
  #   items = [item for item in self.collection if item[key] == value]
  #   return items[0]

  # def fetch_all(self):
  #   """
  #     method to fetch all items objects
  #   """
  #   return self.collection

  # def delete(self, id):
  #   """
  #     method to delete item object
  #   """
  #   item = self.find('id', id)
  #   self.collection.remove(item)