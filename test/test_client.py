from ..client.client import main
import unittest
from unittest.mock import patch

class TestClient(unittest.TestCase):

    @patch('builtins.input', side_effect=['test_auth_token'])
    @patch('requests.get')
    def test_main(self, mock_get, mock_input):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {"auth_token": "test_auth_token"}

        main()

        # Assert that the mock_get function was called with the correct URL
        mock_get.assert_called_once_with("http://localhost:8000/authenticate")

        # Assert that the input function was called once
        mock_input.assert_called_once()

        # Assert that the printed output matches the expected output
        expected_output = "Resource data: {'data': 'This is your resource data'}"
        self.assertEqual(expected_output, self.output.getvalue().strip())

if __name__ == '__main__':
    unittest.main()
