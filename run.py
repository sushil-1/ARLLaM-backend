from fastapi import FastAPI
import nest_asyncio
from pyngrok import ngrok
import uvicorn
from api import app

ngrok_tunnel = ngrok.connect(8000)
ngrok_tunnel.public_url = "https://explicitly-moved-mustang.ngrok-free.app"
print('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, port=8000)