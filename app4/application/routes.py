  
from flask import Flask, render_template, Response, redirect, url_for
import random, string
import requests
from application import app

@app.route('/app4', methods=['POST'])
def app4():
  data1 = requests.get('http://app1')
  if data1.text == '22 April':
    output = "You share my birthday"
  else:
    output = "Unlucky you do not share my birthday"
  
  return Response(output,mimetype='text/plain')
