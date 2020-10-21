import json
import  unittest
from app import app, requests
import mock
# set our application to testing mode
app.testing = True

class TestApi(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_healthcheck(self):
        result = self.app.get('/api/health')
        self.assertEqual(result.status_code,200)

    def test_encrypt_without_data(self):
        api_response = self.app.get('/api/encrypt')
        result = api_response.get_json()
        self.assertEqual(api_response.status_code,400)
        self.assertEqual(result['status'],'error')

    def test_encrypt_with_data_blank(self):
        api_response = self.app.get('/api/encrypt' , json=dict())
        result = api_response.get_json()
        self.assertEqual(api_response.status_code,400)
        self.assertEqual(result['status'],'error')

    def test_encrypt_with_data(self):
        api_response = self.app.get('/api/encrypt', json=dict(input='My String to encrypt'))
        result = api_response.get_json()
        self.assertEqual(api_response.status_code,200)
        self.assertEqual(result['status'],'success')
        self.assertEqual(result['output'],'TXkgU3RyaW5nIHRvIGVuY3J5cHQ=')

    def test_decrypt_without_data(self):
        api_response = self.app.get('/api/decrypt')
        result = api_response.get_json()
        self.assertEqual(api_response.status_code,400)
        self.assertEqual(result['status'],'error')
    
    def test_decrypt_with_data_blank(self):
        api_response = self.app.get('/api/decrypt' , json=dict())
        result = api_response.get_json()
        self.assertEqual(api_response.status_code,400)
        self.assertEqual(result['status'],'error')

    def test_decrypt_with_data(self):
        api_response = self.app.get('/api/decrypt', json=dict(input='TXkgU3RyaW5nIHRvIGVuY3J5cHQ='))
        result = api_response.get_json()
        self.assertEqual(api_response.status_code,200)
        self.assertEqual(result['status'],'success')
        self.assertEqual(result['output'],'My String to encrypt')
    
    def test_decrypt_error(self):
        api_response = self.app.get('/api/decrypt', json=dict(input='My String to encrypt'))
        result = api_response.get_json()
        self.assertEqual(api_response.status_code,400)
        self.assertEqual(result['status'],'error')

    def test_encrypt_error(self):
        api_response = self.app.get('/api/encrypt', json=dict(input=''))
        result = api_response.get_json()
        self.assertEqual(api_response.status_code,400)
        self.assertEqual(result['status'],'error')

        

if __name__ == '__main__':
    unittest.main()