
from flask import Flask

app = Flask (__name__)

class Drink(db.Model):
    id = db.Column(db.integer)

def __repr__ (self):
    pass

@app.route('/')
def index():
    return 'Hello'
