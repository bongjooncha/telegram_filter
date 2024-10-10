from sqlmodel import SQLModel, Field
from sqlalchemy import UniqueConstraint

class Chats(SQLModel, table =True):
    id: int = Field(primary_key=True)
    name: str = Field(nullable=False)

    class Config:
        json_schema_extra = {
            'example': {
                'id': 1001738234843,
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
                'id': 1001738234843,
                'name': 'Chat Name',
                'group': '일반'
            }
        }