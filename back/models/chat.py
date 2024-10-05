from sqlmodel import SQLModel, Field

class Chats(SQLModel, table =True):
    id: int = Field(primary_key=True)
    name: str = Field(nullable=False)

    class Config:
        json_schema_extra = {
            'example': {
                'id': -1001738234843,
                'name': 'Chat Name'
            }
        }
