from flask import Flask
import os

app = Flask(__name__)
dev = False

app.config.from_pyfile('config.py')

from stocks import routes