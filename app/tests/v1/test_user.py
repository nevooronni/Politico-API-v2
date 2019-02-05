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

  def test_index(self):
    """
      Tesst index welcome route
    """

    res = self.client.get('/api/v1/index', headers={'Content-Type': 'application/json'})
    data = res.get_json()

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['status'], 200)
    self.assertEqual(data['message'], 'Welcome to Politico API web service!')

  def test_signup_with_no_data(self):
    """
      Test sign method up with no data
    """

    res = self.client.post('/api/v1/signup')
    data = res.get_json()

    self.assertEqual(res.status_code, 400)
    self.assertEqual(data['status'], 400)
    self.assertEqual(data['message'], 'No data provided')

  def test_signup_with_empty_data(self):
    """
      Test sign method up with empty data
    """

    user = {}

    res = self.client.post('/api/v1/signup', json=user, headers={'Content-Type': 'application/json'})
    data = res.get_json()

    self.assertEqual(res.status_code, 400)
    self.assertEqual(data['status'], 400)
    self.assertEqual(data['message'], 'No data provided')

  def test_signup_with_missing_fields(self):
    """
      Test signup method with missing fields 
    """

    user = {
      'firstname': 'Neville',
      'lastname': 'Oronni',
      'password': 'flask_is_awesome'
    }

    res = self.client.post('/api/v1/signup', json=user, headers={'Content-Type': 'application/json'})
    data = res.get_json()

    self.assertEqual(res.status_code, 400)
    self.assertEqual(data['status'], 400)
    self.assertEqual(data['message'], 'Invalid data, please fill all required fields')


  def test_signup_with_invalid_email(self):
    """
      Test sign method up with invalid email
    """

    user = {
      'firstname': 'Neville',
      'lastname': 'Oronni',
      'othername': 'Gerald',
      'username': 'nevooronni',
      'email': 'wrong_email',
      'password': 'flask_is_awesome',
      'phoneNumber': '0799244265'
    }

    res = self.client.post('/api/v1/signup', json=user, headers={'Content-Type': 'application/json'})
    data = res.get_json()

    self.assertEqual(res.status_code, 400)
    self.assertEqual(data['status'], 400)
    self.assertEqual(data['message'], 'Invalid data, please fill all required fields')

  def test_signup_with_invalid_password(self):
    """ 
      Test signup method with invalid password
    """

    user = {
      "firstname": "Neville",
      "lastname": "Oronni",
      "othername": "Gerald",
      "username": "nevooronni",
      "email": "nevooronni@gmail.com",
      "password": "afdafs",
      "phoneNumber": "0799244265"
    }

    res = self.client.post('/api/v1/signup', json=user, headers={'Content-Type': 'application/json'})
    data = res.get_json()

    self.assertEqual(res.status_code, 400)
    self.assertEqual(data['status'], 400)
    self.assertEqual(data['message'], 'Invalid data, please fill all required fields')

  def test_signup_with_valid_data(self):
    """
      Test signup with valid data
    """

    user = {
      'firstname': 'Derrick',
      'lastname': 'Chisora',
      'username': 'dero',
      'email': 'derrick@gmail.com',
      'password': 'abcD$234g',
      'phoneNumber': '0799244265'  
    }

    res = self.client.post('/api/v1/signup', json=user, headers={'Content-Type': 'applicatioin/json'})
    data = res.get_json()

    self.assertEqual(res.status_code, 201)
    self.assertEqual(data['status'], 201)
    self.assertEqual(data['message'], 'User created successfully')
    self.assertEqual(data['data']['username'], user['username'])

  def test_signup_with_existing_email(self):
    """
      Test signup with an existing email address
    """

    user_1 = {
      'firstname': 'Frank',
      'lastname': 'Ekirapa',
      'username': 'ekiraps',
      'email': 'frankekirapa254@gmail.com',
      'password': 'abcD$234g',
      'phoneNumber': '0712345678'  
    }

    res_1 = self.client.post('/api/v1/signup', json=user_1, headers={'Content-Type': 'application/json'})
    data_1 = res_1.get_json()

    self.assertEqual(res_1.status_code, 201)
    self.assertEqual(data_1['status'], 201)

    user_2 = {
      'firstname': 'Jane',
      'lastname': 'Onimbo',
      'username': 'janey',
      'email': 'frankekirapa254@gmail.com',
      'password': 'rbcF$214c',
      'phoneNumber': '0712344444'  
    }

    res_2 = self.client.post('/api/v1/signup', json=user_2, headers={'Content-Type': 'application/json'})
    data_2 = res_2.get_json()

    self.assertEqual(res_2.status_code, 409)
    self.assertEqual(data_2['status'], 409)
    self.assertEqual(data_2['message'], 'Error email already exists')

  def test_signup_with_existing_username(self):
    """
      Test sign up with an existing username
    """
    user_1 = {
      'firstname': 'William',
      'lastname': 'Wamarite',
      'username': 'willy',
      'email': 'William@gmail.com',
      'password': 'abcD$234g',
      'phoneNumber': '0712345678'  
    }

    res_1 = self.client.post('/api/v1/signup', json=user_1, headers={'Content-Type': 'application/json'})
    data_1 = res_1.get_json()

    self.assertEqual(res_1.status_code, 201)
    self.assertEqual(data_1['status'], 201)

    user_2 = {
      'firstname': 'Paul',
      'lastname': 'Davis',
      'username': 'willy',
      'email': 'william@gmail.com',
      'password': 'rbcF$214c',
      'phoneNumber': '0712344444'  
    }

    res_2 = self.client.post('/api/v1/signup', json=user_2, headers={'Content-Type': 'application/json'})
    data_2 = res_2.get_json()

    self.assertEqual(res_2.status_code, 409)
    self.assertEqual(data_2['status'], 409)
    self.assertEqual(data_2['message'], 'Error username already exists')

  
  def test_refresh_access_token_with_no_token(self):
    """
      Test refresh access token method without passing refresh token
    """

    res = self.client.post('/api/v1/refresh-token')
    data = res.get_json()

    self.assertEqual(res.status_code, 401)
    self.assertEqual(data['msg'], 'Missing Authorization Header')

  def test_refresh_access_token_with_token(self):
    """
      Test refresh access token method with access token
    """

    user = {
      'firstname': 'Diana',
      'lastname': 'Mwiti',
      'username': 'diana',
      'email': 'diana@gmail.com',
      'password': 'abcD$234g',
      'phoneNumber': '0799244265'  
    }

    res_1 = self.client.post('/api/v1/signup', json=user, headers={'Content-Type': 'application/json'})
    data_1 = res_1.get_json()

    self.assertEqual(res_1.status_code, 201)
    self.assertEqual(data_1['status'], 201)

    res = self.client.post('/api/v1/refresh-token', headers={'Authorization': 'Bearer {}'.format(data_1['access_token'])})
    data = res.get_json()

    self.assertEqual(res.status_code, 422)
    self.assertEqual(data['msg'], 'Only refresh tokens are allowed')

  def test_refresh_access_token(self):
    """
      Test refresh access token
    """

    user = {
      'firstname': 'Micheal',
      'lastname': 'Omondi',
      'username': 'omosh',
      'email': 'micheal@gmail.com',
      'password': 'abcD$234g',
      'phoneNumber': '0799244265'  
    }

    res_1 = self.client.post('/api/v1/signup', json=user, headers={'Content-Type': 'application/json'})
    data_1 = res_1.get_json()

    self.assertEqual(res_1.status_code, 201)
    self.assertEqual(data_1['status'], 201)

    res = self.client.post('/api/v1/refresh-token', headers={'Authorization': 'Bearer {}'.format(data_1['refresh_token'])})
    data = res.get_json()

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['status'], 200)
    self.assertEqual(data['message'], 'Token refreshed succesfully')
