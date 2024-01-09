from fastapi import FastAPI, HTTPException
from dashboardx.helpers import *
from dashboardx.models import *
from dashboardx.conversations import conversation_response_by_index
import logging
from dotenv import load_dotenv
import os

load_dotenv('.env')

logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

logger.info('Logging working')

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/get_dashboard_by_id/{dashboard_id}")
def read_item(dashboard_id: str = None, query_param: str = None):
    if(dashboard_id!= None): data = get_dashboard_by_id(dashboard_id)
    logger.info(data)
    return data

@app.get("/dashboards/get_all")
def read_item():
    data = get_all_dashboards()
    logger.info(data)
    return data

@app.put("/update_dashboard/")
def update_dashboard(dashboard: Dashboard):
    dashboard = update_dashboard_by_id(dashboard._id, dashboard)
    return dashboard

@app.put("/get_response/}")
def send_message(conversation: Conversation):
    response = get_bot_response(conversation)
    messages = response
    
    return response

