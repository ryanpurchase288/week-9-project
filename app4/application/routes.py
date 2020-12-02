  
from flask import Flask, render_template, Response, redirect, url_for, request
import random, string
import requests
from application import app

@app.route('/app4', methods=['POST'])
def app4():
  data1 = request.data.decode('utf-8')
  if data1 == '22 April':
    output = "You share my birthday"
  elif '22' in data1:
    output ='You share the same day'
  else:
    output = "Unlucky you do not share my birthday"
  
  return Response(output,mimetype='text/plain')
