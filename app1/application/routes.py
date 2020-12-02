from flask import render_template, redirect, url_for
from application import app
import requests


@app.route('/')
@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', title='Home')

@app.route('/get/random',methods=['GET','POST'])
def generate():
    response1 = requests.get("http://app2:5001/month") 
    response2 = requests.get("http://app3:5002/day")    
    response3 = requests.post("http://app4:5003/app4",  data=(response2.text+" "+response1.text) ) 
    
    return render_template('display.html',title='Home',data1=response2.text, data2=response1.text, data3=response3.text)