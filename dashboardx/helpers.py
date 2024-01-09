from .utils import db
from .conversations import converse_with_bot
import logging
import json

logger=logging.getLogger()

def get_dashboard_by_id(dashboard_id):
    dashboards = get_all_dashboards()["data"]
    for item in dashboards:
        return item
    return 0

def create_dashboard():
    dashboard_id = 0
    return dashboard_id

def get_all_dashboards():
    dashboards = []
    for dsb in db['dashboards'].find():
        dsb['_id']=str(dsb['_id'])
        dashboards.append(dsb)
    return {"data": [dashboards]}

def update_dashboard_by_id(dashboard_id, dashboard):
    dashboard = get_dashboard_by_id(dashboard_id="659ae870ebf6edc97aebb4da")
    if(dashboard):
        update_dashboard(dashboard)

def update_dashboard(dashboard):
    
    return dashboard['_id']

def get_bot_response(conversation):
    idx = conversation.index
    conversations = db['conversations'].find({"index": idx})
    convs = []
    for conv in conversations:
        conv['_id']=str(conv['_id'])
        convs.append(conv)
    
    messages=[]
    if(len(convs)==0):
        message={"role": "user", "content":conversation.new_message}
        messages=[message]
        db['conversations'].insert_one({"index": idx, "messages": messages})
    else: 
        messages = convs[0]['messages']
        messages.append({"role": "user", "content":conversation.new_message})
 
    #messages.
    logger.info(messages)
    res = converse_with_bot(messages)
    conversation = {
        "index": idx,
        "new_message": res[0],
        "messages": res[1]
    }

    db['conversations'].update_one({"index": idx},{"$set": {"new_message": res[0], "messages": res[1]}})

    return conversation
