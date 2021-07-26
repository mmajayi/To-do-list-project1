import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = str(os.urandom(16))

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:testpass@34.142.88.11/car'

db = SQLAlchemy(app)

from application import routes