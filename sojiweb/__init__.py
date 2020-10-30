from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail
import os

app = Flask(__name__)
dev = False

if dev:
    app.config.from_pyfile('local_config.py')
else:
    app.config.from_pyfile('config.py')

#protect against malicious attacks
db = SQLAlchemy(app)
mail = Mail()
mail.init_app(app)

from sojiweb import routes