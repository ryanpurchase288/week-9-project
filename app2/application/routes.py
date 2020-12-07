from application import app
from flask import request, Response
from random import randint
import random

@app.route('/month', methods=['GET'])
def month():
    return Response(str(random.randint(1990,2000)), mimetype='text/plain')