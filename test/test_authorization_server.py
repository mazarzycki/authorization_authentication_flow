import unittest
from ..authorization_server.authorization_server import app
from unittest.mock import patch

class TestAuthorizationServer(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    @patch('secrets.token_hex', return_value='test_auth_token')
    def test_authenticate(self, mock_token_hex):
        response = self.app.get('/authenticate')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"auth_token": "test_auth_token"})
        mock_token_hex.assert_called_once()

if __name__ == '__main__':
    unittest.main()
