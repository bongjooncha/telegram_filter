from fastapi import FastAPI, Depends, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text,select

from database.connection import conn, get_session
from function.tele_func import TelegramFunction
from models.chat import Chats

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React 앱의 주소
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

auth = TelegramFunction()

@app.on_event("startup")
def startup():
    conn()

@app.get("/synchronize_chat_ids")
async def synchronize_chat_ids(session = Depends(get_session)):
    #chat table 비우기
    session.execute(text("DELETE FROM chats"))
    session.commit()

    await auth.client.connect()
    dialogs = await auth.read_chat_ids()
    for dialog in dialogs:
        try:
            chat_id = dialog.entity.id
            chat_name = dialog.entity.title
            new_chat = Chats(id = chat_id, name = chat_name)
            session.add(new_chat)
        except AttributeError:
            pass
    session.commit()
    return {"message": "chat ids synchronized commplitly"}

@app.get("/get_all_chat_ids")
async def get_all_chat_ids(session=Depends(get_session)):
    all_chats = session.execute(select(Chats))
    chats = all_chats.scalars().all()
    return chats




