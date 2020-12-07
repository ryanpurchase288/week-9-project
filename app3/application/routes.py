from application import app
from flask import Flask, Response,  url_for
import random, string
import requests
from random import randint



@app.route('/day', methods=['GET'])
def day():
  day=['Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday']
  return Response(day[randint(0,4)], mimetype='text/plain')

