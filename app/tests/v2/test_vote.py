from flask import json
from .base_test import BaseTest
from app.api.v2.models.office_model import table
from app.api.v2.models.candidates_model import table
from app.api.v2.models.candidates_model import table
from app.api.v2.models.votes_model import table
from app.api.v2.models.user_model import table

class TestVote(BaseTest):
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

    self.super_user2 = {
      'firstname': 'Neville',
      'lastname': 'Oronni',
      'email': 'neville@gmail.com',
      'password': 'abcD$234g',
      'phonenumber': '0745992344'
    }

    self.super_user3 = {
      'firstname': 'Frank',
      'lastname': 'Ekirapa',
      'email': 'frank@gmail.com',
      'password': 'abcD$234g',
      'phonenumber': '0745123899'
    }

    self.super_user4 = {
      'firstname': 'Paul',
      'lastname': 'Wanjala',
      'email': 'paul@gmail.com',
      'password': 'abcD$234g',
      'phonenumber': '0748888888'
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
      'user_id': 1
    }

    self.candidate_2 = {
      'user_id': 2
    }

    self.vote = {
      'voter': 1,
      'office': 2,
      'candidate': 1,
    }

    self.vote_2 = {
      'voter': 2,
      'office': 2,
      'candidate': 1,
    }

    self.vote_3 = {
      'voter': 3,
      'office': 2,
      'candidate': 2,
    }

    self.vote_4 = {
      'voter': 4,
      'office': 2, 
      'candidate': 1,
    }

    #signup
    self.res_1 = self.client.post('/api/v2/auth/signup', json=self.super_user, headers={'Content-Type': 'application/json'})
    self.res_12 = self.client.post('/api/v2/auth/signup', json=self.super_user2, headers={'Content-Type': 'application/json'})
    self.res_13 = self.client.post('/api/v2/auth/signup', json=self.super_user3, headers={'Content-Type': 'application/json'})
    self.res_14 = self.client.post('/api/v2/auth/signup', json=self.super_user3, headers={'Content-Type': 'application/json'})
    self.data_14 = self.res_1.get_json()
    self.data_14_token = self.get_value(self.data_14, 'access_token')

    #create two offices
    self.res_4 = self.client.post('/api/v2/offices', json=self.office, headers={'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(self.data_14_token)})
    self.data_4 = self.res_1.get_json()
    
    self.res_5 = self.client.post('/api/v2/offices', json=self.office_3, headers={'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(self.data_14_token)})
    self.data_5 = self.res_1.get_json()

    #create two candidates
    self.res_4 = self.client.post('/api/v2/offices/2/register', json=self.candidate, headers={'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(self.data_14_token)})
    self.data_4 = self.res_1.get_json()
    
    self.res_5 = self.client.post('/api/v2/offices/2/register', json=self.candidate_2, headers={'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(self.data_14_token)})
    self.data_5 = self.res_1.get_json()


  def get_value(self, data, key):
    new_value = data['data'][0]
    return new_value[key]
    
  def get_value2(self, data, key):
    new_value = data['data'][0]
    party_value = new_value['office'][0]
    party_field = party_value['id']
    return party_value[key]

  def test_create_vote(self):
    """
      Test create vote method
    """

    res = self.client.post('/api/v2/votes', json=self.vote, headers={'Authorization': 'Bearer {}'.format(self.data_14_token)})
    data = res.get_json()
    print(data)

    self.assertEqual(res.status_code, 201)
    self.assertEqual(data['status'], 201)
    self.assertEqual(self.get_value(data, 'message'), 'voted succesfully')

  def test_fetch_results(self):
    """
      Test fetch election results method
    """

    res = self.client.post('/api/v2/votes', json=self.vote, headers={'Authorization': 'Bearer {}'.format(self.data_14_token)})
    data = res.get_json()
    self.assertEqual(res.status_code, 201)
    self.assertEqual(data['status'], 201)

    res_2 = self.client.post('/api/v2/votes', json=self.vote_2, headers={'Authorization': 'Bearer {}'.format(self.data_14_token)})
    data_2 = res.get_json()
    self.assertEqual(res_2.status_code, 201)

    res_3 = self.client.post('/api/v2/votes', json=self.vote_3, headers={'Authorization': 'Bearer {}'.format(self.data_14_token)})
    data_3 = res.get_json()
    self.assertEqual(res_3.status_code, 201)

    res_4 = self.client.post('/api/v2/votes', json=self.vote_4, headers={'Authorization': 'Bearer {}'.format(self.data_14_token)})
    data_4 = res.get_json()
    self.assertEqual(res_4.status_code, 201)

    response = self.client.get('/api/v2/office/2/result', headers={'Authorization': 'Bearer {}'.format(self.data_14_token)})
    result = response.get_json()
    self.assertEqual(response.status_code, 200)
    self.assertEqual(result['status'], 200)
    self.assertEqual(self.get_value(result, 'message'), 'fetched votes successfully')
