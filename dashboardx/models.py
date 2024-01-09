from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class Component(BaseModel):
    _id: str
    name: str
    type: str
    data: Dict[str, float]

class Dashboard(BaseModel):
    _id: str
    name: str
    filters: Optional[list]
    rows: Optional[List[List[Component]]]= Field(..., max_items=4)

class Message(BaseModel):
    _id: str
    role: str
    component: bool
    content: str

class Conversation(BaseModel):
    _id: str
    index: str
    new_message: Optional[str] = None
    messages: Optional[List[Message]]