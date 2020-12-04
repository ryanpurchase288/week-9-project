from application import app
from flask import Flask, Response,  url_for
import random, string
import requests



@app.route('/day', methods=['GET'])
def day():
  return Response(str(random.randint(20,25)), mimetype='text/plain')

