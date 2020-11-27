import requests
from flask import url_for
from flask_testing import TestCase
from application import app
class TestBase(TestCase):
  def create_app(self):
    return app
class TestViews(TestBase):
  def test_app3(self):
    response = self.client.get(url_for('day'))
    self.assertEquals(response.status_code,200)