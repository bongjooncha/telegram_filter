from sqlmodel import SQLModel, Field, Column
from typing import List, Dict, Any
from sqlalchemy import UniqueConstraint, JSON
from pydantic import BaseModel

class Chats(SQLModel, table =True):
    id: int = Field(primary_key=True)
    name: str = Field(nullable=False)

    class Config:
        json_schema_extra = {
            'example': {
                'id': '1001738234843',
                'name': 'Chat Name'
            }
        }
        
class ChatGroups(SQLModel, table = True):
    id: int = Field(primary_key=True)
    name: str = Field(nullable=False)
    group: str = Field(primary_key=True)

    __table_args__ = (UniqueConstraint('name', 'group'),)
    class Config:
        json_schema_extra = {
            'example': {
                'id': '1001738234843',
                'name': 'Chat Name',
                'group': '일반'
            }
        }


class MessageRequest(BaseModel):
    chat_id: int
    message: str

class Filters(SQLModel, table =True):
    filter_name: str = Field(primary_key=True)
    tr_id_name: List[Dict[str, Any]] = Field(sa_column=Column(JSON))
    rr_id_name: List[Dict[str, Any]] = Field(sa_column=Column(JSON))
    words: List[str] = Field(sa_column=Column(JSON))
    on_off: bool = Field(default=False)

    class Config:
        arbitrary_types_allowed = True


class Bot(SQLModel, table = True):
    name: str = Field(primary_key=True)
    token: str = Field(nullable=False)