from pymongo import MongoClient
from .config import config

client = MongoClient(config.get('DB_CONNECTION_URL'))
db = client[config.get('DATABASE_NAME')]