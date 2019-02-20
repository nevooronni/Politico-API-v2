# from flask import json
# from .base_test import BaseTest
# from app.api.v2.models.office_model import offices
# from app.api.v2.models.user_model import users


# class TestPoliticalParty(BaseTest):
#   """
#     Test class for a political party
#   """

#   def setUp(self):
#     """
#       setup method for initializing varialbes
#     """
#     super().setUp()

#     self.super_user = {
#       'firstname': 'Donald',
#       'lastname': 'Trump',
#       'email': 'trump@gmail.com',
#       'password': 'abcD$234g',
#       'phoneNumber': '0781818181'
#     }

#     self.office = {
#       'type': 'Executive',
#       'name': 'Vice President',
#     }

#     self.office_2 = {
#       'type': 'Legistlature',
#       'name': 'Vice President',
#     }

#     self.office_3 = {
#       'type': 'Legistlature',
#       'name': 'MP Starehe constituency',
#     }

#     self.office_with_no_name = {
#       'type': 'Executive',
#     }

#     self.office_with_empty_name = {
#       'type': 'Executive',
#       'name': '',
#     }

#     self.res_1 = self.client.post('/api/v2/auth/signup', json=self.super_user, headers={'Content-Type': 'application/json'})
#     self.data_1 = self.res_1.get_json()
#     self.data_1_token = self.get_value(self.data_1, 'access_token')


#   def get_value(self, data, key):
#     new_value = data['data'][0]
#     return new_value[key]
    
#   def get_value2(self, data, key):
#     new_value = data['data'][0]
#     party_value = new_value['office'][0]
#     party_field = party_value['id']
#     return party_value[key]

#   def signup(self):
#     """ 
#       method to sign up user and get access token 
#     """
        
#     res = self.client.post('/api/v2/auth/signup', json=self.super_user)
#     data = res.get_json()
#     data_token = self.get_value(data, 'access_token')

#     self.access_token = data_token

#     return self.access_token

#   def tearDown(self):
#     """
#       teardown method empty all initialized variables
#     """

#     offices.clear()
#     super().tearDown()
#     users.clear()

#   def test_create_office_with_no_data(self):
#     """
#       Test create office with no data provided
#     """
    
#     res = self.client.post('/api/v2/offices', headers={'Authorization': 'Bearer {}'.format(self.data_1_token)})
#     data = res.get_json()

#     self.assertEqual(res.status_code, 400)
#     self.assertEqual(data['status'], 400)
#     self.assertEqual(data['message'], 'No data provided')

#   def test_create_party_with_empty_data(self):
#     """
#       Test create office method with emtpy data
#     """

#     office = {}
#     res = self.client.post('/api/v2/offices', json=json.dumps(office), headers={'Authorization': 'Bearer {}'.format(self.data_1_token)})
#     data = res.get_json()

#     self.assertEqual(res.status_code, 400)
#     self.assertEqual(data['status'], 400)
#     self.assertEqual(data['message'], 'Invalid data, please fill all required fields')

#   def test_create_office_with_missing_fields(self):
#     """
#       Test create office method with missing fields
#     """

#     res = self.client.post('/api/v2/offices', json=self.office_with_no_name, headers={'Authorization': 'Bearer {}'.format(self.data_1_token)})
#     data = res.get_json()

#     self.assertEqual(res.status_code, 400)
#     self.assertEqual(data['status'], 400)
#     self.assertEqual(data['message'], 'Invalid data, please fill all required fields')

#   def test_create_office_with_empty_fields(self):
#     """
#       Test create office method with empty fields
#     """

#     res = self.client.post('/api/v2/offices', json=self.office_with_empty_name, headers={'Authorization': 'Bearer {}'.format(self.data_1_token)})
#     data = res.get_json()

#     self.assertEqual(res.status_code, 400)
#     self.assertEqual(data['status'], 400)
#     self.assertEqual(data['message'], 'Invalid data, please fill all required fields')

#   def test_create_offices_with_existing_name(self):
#     """
#       Test method to create office with an existing name
#     """

#     data_1 = self.res_1.get_json()
#     data_1_token = self.get_value(data_1, 'access_token')

#     res = self.client.post('/api/v2/offices', json=self.office, headers={'Authorization': 'Bearer {}'.format(data_1_token)})
#     data_1 = res.get_json()

#     self.assertEqual(res.status_code, 201)
#     self.assertEqual(data_1['status'], 201)

#     res_2 = self.client.post('/api/v2/offices', json=self.office_2, headers={'Authorization': 'Bearer {}'.format(data_1_token)})
#     data_2 = res_2.get_json()

#     self.assertEqual(res_2.status_code, 409)
#     self.assertEqual(data_2['status'], 409)
#     self.assertEqual(data_2['message'], 'Error office already exists')

#   def test_create_office(self):
#     """
#       Test create office method
#     """
#     data_1 = self.res_1.get_json()

#     data_1_token = self.get_value(data_1, 'access_token')

#     res = self.client.post('/api/v2/offices', json=self.office, headers={'Authorization': 'Bearer {}'.format(data_1_token)})
#     data = res.get_json()

#     self.assertEqual(res.status_code, 201)
#     self.assertEqual(data['status'], 201)
#     self.assertEqual(self.get_value(data, 'message'), 'office created succesfully')

#   def test_fetch_specific_office(self):
#     """
#       Test method for fetching a specific office
#     """

#     self.client.post('/api/v2/offices', json=self.office, headers={'Authorization': 'Bearer {}'.format(self.data_1_token)})
#     self.client.post('/api/v2/offices', json=self.office_3, headers={'Authorization': 'Bearer {}'.format(self.data_1_token)})

#     res = self.client.get('/api/v2/offices/2', headers={'Authorization': 'Bearer {}'.format(self.data_1_token)})
#     data = res.get_json()

#     self.assertEqual(res.status_code, 200)
#     self.assertEqual(data['status'], 200)
#     self.assertEqual(self.get_value2(data, 'id'), 2)

#   def test_fetch_non_existent_office(self):
#     """
#       Test method for fetching an office that doesn't exist
#     """
#     res = self.client.get('/api/v2/offices/14', headers={'Authorization': 'Bearer {}'.format(self.data_1_token)})
#     data = res.get_json()

#     self.assertEqual(res.status_code, 404)
#     self.assertEqual(data['status'], 404)
#     self.assertEqual(self.get_value(data, 'message'), 'office not found')

  
#   def test_fetch_all_offices(self):
#     """ 
#       Test method for fetching all offices
#     """
#     self.client.post('/api/v2/offices', json=self.office, headers={'Authorization': 'Bearer {}'.format(self.data_1_token)})
#     self.client.post('/api/v2/offices', json=self.office_3, headers={'Authorization': 'Bearer {}'.format(self.data_1_token)})

#     res = self.client.get('/api/v2/offices', headers={'Authorization': 'Bearer {}'.format(self.data_1_token)})
#     data = res.get_json()

#     office_dict = data['data'][0]
#     office = office_dict['offices']
#     self.assertEqual(res.status_code, 200)
#     self.assertEqual(data['status'], 200)
#     self.assertEqual(len(office), 2)

#   def test_delete_office(self):
#     """
#       Test method for deleting an office successfully
#      """

#     self.client.post('/api/v2/offices', json=self.office, headers={'Authorization': 'Bearer {}'.format(self.data_1_token)})
#     self.client.post('/api/v2/offices', json=self.office_3, headers={'Authorization': 'Bearer {}'.format(self.data_1_token)})

#     res = self.client.delete('/api/v2/offices/2', headers={'Authorization': 'Bearer {}'.format(self.data_1_token)})
#     data = res.get_json()

#     self.assertEqual(res.status_code, 200)
#     self.assertEqual(data['status'], 200)
#     self.assertEqual(self.get_value(data, 'message'), 'office deleted successfully')

