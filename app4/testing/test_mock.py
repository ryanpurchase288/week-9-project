from unittest.mock import patch
import unittest
import requests

from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
   
    def test_get(self):
        with patch('requests.post') as g:
            g.return_value.text = "22 April"
                
            response = self.client.post(url_for('app4'))
            self.assertIn(b'You share my birthday',response.data)
            self.assertEqual(response.status_code, 200)