from application import app
from flask import request, Response
from random import randint

@app.route('/month', methods=['GET'])
def month():
    month = [ 'March', 'April','May','June','July']
    return Response(month[randint(0,4)], mimetype='text/plain')