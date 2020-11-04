import os
from dotenv import load_dotenv
from stocks import dev
load_dotenv()

if dev:
    SECRET_KEY = os.getenv('SECRET_KEY')
else:
    SECRET_KEY = os.environ.get('SECRET_KEY')

UPLOAD_FOLDER = 'downloads/'