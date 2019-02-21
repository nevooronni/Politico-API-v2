from flask import json
from .base_test import BaseTest
from app.api.v2.models.office_model import table
from app.api.v2.models.candidates_model import table
from app.api.v2.models.user_model import table


class TestPoliticalParty(BaseTest):
  """
    Test class for a political party
  """

  def setUp(self):
    """
      setup method for initializing varialbes
    """
    super().setUp()

    self.super_user = {
      'firstname': 'Donald',
      'lastname': 'Trump',
      'email': 'trump@gmail.com',
      'password': 'abcD$234g',
      'phonenumber': '0781818181'
    }

    self.office = {
      'type': 'Executive',
      'name': 'Vice President',
    }

    self.office_3 = {
      'type': 'Legistlature',
      'name': 'MP Starehe constituency',
    }

    self.political_party = {
      'name': 'Jubilee Party',
      'hqAddress': 'Pangani, Nairobi',
      'logoUrl': 'app/img/jubilee.jpg'
    }

    self.political_party2 = {
      'name': 'Nasa Party',
      'hqAddress': 'Karen, Nairobi',
      'logoUrl': 'app/img/nasa.jpg'
    }

    self.candidate = {
      'user_id': 2
    }

    #signup
    self.res_1 = self.client.post('/api/v2/auth/signup', json=self.super_user, headers={'Content-Type': 'application/json'})
    self.data_1 = self.res_1.get_json()
    self.data_1_token = self.get_value(self.data_1, 'access_token')

    #create two offices
    self.res_4 = self.client.post('/api/v2/offices', json=self.office, headers={'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(self.data_1_token)})
    self.data_4 = self.res_1.get_json()
    print(self.data_4)
    
    self.res_5 = self.client.post('/api/v2/offices', json=self.office_3, headers={'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(self.data_1_token)})
    self.data_5 = self.res_1.get_json()

  def get_value(self, data, key):
    new_value = data['data'][0]
    return new_value[key]
    
  def get_value2(self, data, key):
    new_value = data['data'][0]
    party_value = new_value['office'][0]
    party_field = party_value['id']
    return party_value[key]

  def test_create_candidate(self):
    """
      Test create candidate method
    """

    res = self.client.post('/api/v2/offices/2/register', json=self.candidate, headers={'Authorization': 'Bearer {}'.format(self.data_1_token)})
    data = res.get_json()
    print(data)

    self.assertEqual(res.status_code, 201)
    self.assertEqual(data['status'], 201)
    self.assertEqual(self.get_value(data, 'message'), 'candidate created succesfully')