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
   
    def test_app4(self):
            response = self.client.post('/app4', data="22 April")
            self.assertIn(b'You share my birthday',response.data)
            self.assertEqual(response.status_code, 200)

    def test_appday(self):
            response = self.client.post('/app4', data="22")
            self.assertIn(b'You share the same day',response.data)
            self.assertEqual(response.status_code, 200)

    def test_appNo(self):
            response = self.client.post('/app4', data="21 May")
            self.assertIn(b'Unlucky you do not share my birthday',response.data)
            self.assertEqual(response.status_code, 200)