from .utils import db, openai_client
import logging

logger = logging.getLogger()
col = db['conversations']

def get_conversation_by_index(index):
    try:
        res = col.find_one()
    except:
        logger.info('mongo error')
    
    conversations = [i for i in res]
    
    #conversation = conversations[0]
    if(conversation['messages'].length==0):
        conversation = {
            "index": index,
            "new_message": {"role": "user", "content": "Hi there :D"}, 
            "messages": [{"role": "user", "content": "Hi there :D"}]
        }
    return conversation
    
def conversation_response_by_index(conv):
    index = conv.index
    conversation = get_conversation_by_index(index)
    res = converse_with_bot(conversation['messages'])
    db['conversations'].update_one({"index": index}, {"$set": {'new_message': res[0], 'messages':res[1]}})
    return {'new_message': res[0], 'messages':res[1]}

def get_starter_message():
    message = "Hi There"
    return {"role":"user", "content":message}

def converse_with_bot(messages):
    response = openai_client.chat.completions.create(
		messages=messages,
    model="gpt-3.5-turbo",
	)
    response_message = {
        "role": response.choices[0].message.role,
        "content" : response.choices[0].message.content
    }
    messages.append(response_message)
    return response_message, messages
