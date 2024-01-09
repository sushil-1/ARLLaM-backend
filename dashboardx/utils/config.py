from dotenv import load_dotenv
import os

base_path = os.path.dirname(__file__)
env_path = '/.env'

load_dotenv(
    base_path+env_path
)

config = dict()
config['DB_CONNECTION_URL'] = os.getenv('DB_CONNECTION_URL')
config['DATABASE_NAME'] = os.getenv('DATABASE_NAME')
config['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')