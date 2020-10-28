from sojiweb import db
from datetime import datetime

# pylint: skip-file

### Currently not in use
class RealMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.String(10000), nullable=False)
    newsletter = db.Column(db.Boolean(1), nullable=False)

class EmailList(db.Model):
    __tablename__ = 'EmailList'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
