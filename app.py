import time

import redis
from flask import Flask

@app.route('/')
def hello_world():
    return 'Hello, World!'
