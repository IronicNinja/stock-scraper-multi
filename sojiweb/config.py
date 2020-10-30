import os

SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = os.environ.get('HEROKU_POSTGRESQL_NAVY_URL')
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 'sojiremora@gmail.com'
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')