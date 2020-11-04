import os
from dotenv import load_dotenv
from stocks import dev
import redis
load_dotenv()

if dev:
    SECRET_KEY = os.getenv('SECRET_KEY')
else:
    SECRET_KEY = os.environ.get('SECRET_KEY')

SESSION_TYPE = 'redis'
SESSION_REDIS = redis.from_url(os.getenv('SESSION_REDIS'))
