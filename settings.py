import os
from os.path import join, dirname
from dotenv import load_dotenv
 
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
 
api_key=os.getenv('API_KEY')
api_key_secret=os.getenv('API_KEY_SECRET')
bearer_token=os.getenv('BEARER_TOKEN')
access_token=os.getenv('ACCESS_TOKEN')
access_token_secret=os.getenv('ACCESS_TOKEN_SECRET')