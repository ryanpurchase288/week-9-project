  
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestMonth(TestBase):
    def test_month(self):
        month = [b'January', b'February', b'March', b'April',b'May',b'June',b'July',b'August',b'September',b'October', b'November', b'December']
        response = self.client.get(url_for('month'))
        self.assertIn(response.data, month)