from resource_api import app
import unittest
from unittest.mock import patch

class TestResourceAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    @patch('secrets.token_hex', return_value='test_auth_token')
    @patch('requests.get')
    def test_get_resource(self, mock_get, mock_token_hex):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "You have succesfully connected to the database. This is your resource data."}

        headers = {"Authorization": "Bearer test_auth_token"}
        response = self.app.get('/resource', headers=headers)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"data": "You have succesfully connected to the database. This is your resource data."})

if __name__ == '__main__':
    unittest.main()
