from flask import json, make_response
from .base_test import BaseTest


class TestUser(BaseTest):
  """
    Test class for user endpoints
  """

  def setUp(self):
    """
      Initialize variables to be used for user tests
    """
    super().setUp()

  def get_value(self, data, key):
    new_value = data['data'][0]
    return new_value[key]
    
  def get_value2(self, data, key):
    new_value = data['data'][0]
    user_value = new_value['user']
    return user_value[key]
    
  # def signup(self):
  #   """ 
  #     method to sign up user and get access token 
  #   """
        
  #   res = self.client.post('/api/v1/signup', json=self.super_user)
  #   data = res.get_json()
  #   data_token = self.get_value(data, 'access_token')

  #   self.access_token = data_token

  def test_index(self):
    """
      Tesst index welcome route
    """

    res = self.client.get('/api/v2/index', headers={'Content-Type': 'application/json'})
    data = res.get_json()

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['status'], 200)
    self.assertEqual(data['message'], 'welcome to Politico API Web service, use the base url: https://politco-api.herokuapp.com/api/v1 for posting your requests')
