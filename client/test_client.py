from client import main
import unittest
from unittest.mock import patch, MagicMock

class TestClient(unittest.TestCase):

    @patch('builtins.input', side_effect=['test_auth_token'])
    @patch('requests.get')
    def test_main(self, mock_get, mock_input):
        # Mock for the first requests.get call (auth_server_url)
        mock_auth_response = MagicMock()
        mock_auth_response.status_code = 200
        mock_auth_response.json.return_value = {"auth_token": "test_auth_token"}

        # Mock for the second requests.get call (resource_api_url)
        mock_resource_response = MagicMock()
        mock_resource_response.status_code = 200
        mock_resource_response.json.return_value = {"data": "This is your resource data"}

        # Configure side_effect for requests.get
        mock_get.side_effect = [mock_auth_response, mock_resource_response]

        main()

        # Assert that the mock_get function was called with the correct URLs
        mock_get.assert_any_call("http://localhost:8000/authenticate")
        mock_get.assert_any_call("http://localhost:8001/resource", headers={"Authorization": "Bearer test_auth_token"})

        # Assert that the input function was called once
        mock_input.assert_called_once()

if __name__ == '__main__':
    unittest.main()
