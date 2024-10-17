from fastapi import FastAPI, Depends, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text,select,delete
from typing import List

import config

from database.connection import conn, get_session
from function.tele_func import TelegramFunction
from models.chat import Chats, ChatGroups, MessageRequest
from telethon import events

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React 앱의 주소
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

auth = config.Config.CLIENT_NAME

@app.on_event("startup")
async def startup():
    await auth.start()
    conn()


@auth.on(events.NewMessage(chats=2149529921))
async def handler(event):
    print(f"새 메시지: {event.message.text}")

@app.get("/synchronize_chat_ids")
async def synchronize_chat_ids(session = Depends(get_session)):
    #chat table 비우기
    session.execute(text("DELETE FROM chats"))
    session.commit()

    dialogs = await TelegramFunction.read_chat_ids(auth)
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

@app.post("/send_message")
async def send_message(request: MessageRequest):
    try:
        message = await TelegramFunction.send_message(auth,request.chat_id,request.message)
        print(message.message)
        return {"message": f"{message.message}가 {message.peer_id} 로 전송"}
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))


@app.get("/get_all_chat_ids")
async def get_all_chat_ids(session=Depends(get_session)):
    all_chats = session.execute(select(Chats))
    chats = all_chats.scalars().all()
    return chats

@app.get("/get_group_names")
async def get_all_group_names(session=Depends(get_session)):
    unique_groups = session.execute(select(ChatGroups.group).distinct())
    groups = [group[0] for group in unique_groups]
    return groups

@app.get("/get_chat_group/{group}")
async def get_chat_group(group: str, session=Depends(get_session)):
    chat_groups = session.execute(select(ChatGroups).where(ChatGroups.group == group))
    result = chat_groups.scalars().all()
    if not result:
        raise HTTPException(status_code = 404, detail='해당 그룹이 존재하지 않습니다')
    return result

@app.delete("/delete_chat_group/{group}")
async def delete_chat_group(group: str, session=Depends(get_session)):
    delete_stmt = delete(ChatGroups).where(ChatGroups.group == group)
    session.execute(delete_stmt)
    session.commit()
    return {"message": "chat group deleted succesfully"}

@app.post("/edit_chat_group")
async def update_chat_groups(chat_groups: List[ChatGroups], session=Depends(get_session)):
    group_value = chat_groups[0].group
    delete_stmt = delete(ChatGroups).where(ChatGroups.group == group_value)
    session.execute(delete_stmt)
    session.add_all(chat_groups)
    session.commit()
    return {"message": "chat group updated succesfully"}

