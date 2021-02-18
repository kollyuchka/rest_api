import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
DB_NAME = os.getenv('DB_NAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
FLASK_APP = os.getenv('FLASK_APP')
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:' + DB_PASSWORD + '@localhost/' + DB_NAME
SQLALCHEMY_TRACK_MODIFICATIONS = False