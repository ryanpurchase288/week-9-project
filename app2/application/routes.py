from application import app
from flask import request, Response
from random import randint

@app.route('/month', methods=['GET'])
def month():
    month = ['January', 'February', 'March', 'April','May','June','July','August','September','October', 'November', 'December']
    return Response(month[randint(0,11)], mimetype='text/plain')