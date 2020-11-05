import os
from dotenv import load_dotenv
from stocks import dev
import redis
load_dotenv()

SESSION_TYPE = 'redis'
if dev:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SESSION_REDIS = redis.from_url(os.getenv('SESSION_REDIS'))
else:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SESSION_REDIS = redis.from_url(os.environ.get('SESSION_REDIS'))


