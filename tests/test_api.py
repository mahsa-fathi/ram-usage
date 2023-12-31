import unittest
from unittest import TestCase
from unittest.mock import patch
from fastapi.testclient import TestClient
from fastapi import status
from services.api import app


class TestApi(TestCase):

    def setUp(self):
        """Runs before each test"""
        self.client = TestClient(app)

    @patch('services.api.get_module_logger')
    def test_ram_info_float_input(self, patch_module_logger):
        """
        Test if the api gives an error for anything that is not integer
        """
        result = self.client.get(f'/ram/{3.5}')
        self.assertEqual(result.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)

    @patch('services.api.get_module_logger')
    def test_ram_info(self, patch_module_logger):
        """
        Checking if the result of the query is as asked
        When asking for n last memory info, the output list should show n or less than n results (when db is not yet
        filled)
        """
        n = 3
        result = self.client.get(f'/ram/{n}')
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(result.json()), n)


if __name__ == '__main__':
    unittest.main()
