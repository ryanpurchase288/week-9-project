  
from flask import Flask, render_template, Response, redirect, url_for, request
import random, string
import requests
from application import app

@app.route('/app4', methods=['POST'])
def app4():
  data1 = request.data.decode('utf-8')
  if data1 == 'Wednesday 1998':
    output = "You share my birthday on the same year"
  elif 'Wednesday' in data1:
    output ='You share the same day of the week'
  else:
    output = "Unlucky you do not share my birthday"
  
  return Response(output,mimetype='text/plain')
