from pymongo import MongoClient
from openai import OpenAI

config = {
    "DB_CONNECTION_URL": 
    "mongodb+srv://appuser:appuserpassword@appcluster.gbudn6z.mongodb.net/?retryWrites=true&w=majority",
    "OPENAI_API_KEY": "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"
}

client = MongoClient(config['DB_CONNECTION_URL'])
db = client['dashboardx']

openai_client = OpenAI(
    api_key = config['OPENAI_API_KEY']
)

