from flask import Flask
from flask_session import Session
import os

app = Flask(__name__)
dev = False

app.config.from_pyfile('config.py')

sess = Session()
sess.init_app(app)

from stocks import routes