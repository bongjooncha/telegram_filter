from sqlmodel import SQLModel, Session, create_engine
from models.chat import Chats

database_file = 'database.db'
database_url = f'sqlite:///{database_file}'
connect_args = {'check_same_thread': False}
engine_url = create_engine(database_url, connect_args=connect_args, echo=False)

def conn():
    SQLModel.metadata.create_all(engine_url)

def get_session():
    with Session(engine_url) as session:
        yield session