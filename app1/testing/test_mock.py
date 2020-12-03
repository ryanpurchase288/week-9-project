from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app


class TestResponse(TestBase):
    

    def test_generatepage_view(self):

        response = self.client.get(url_for('generate'))
        self.assertEqual(response.status_code, 500)


    def test_postpage_view(self):

        with requests_mock.mock() as g:
            g.get("http://app2:5001/month", text="April")
            g.get("http://app3:5002/day", text="22")
            g.post("http://app4:5003/app4", text="You share my birthday")
            response = self.client.get(url_for('generate'))
            self.assertEqual(response.status_code, 200)