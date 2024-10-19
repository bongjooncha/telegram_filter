from fastapi import APIRouter,  Depends, HTTPException
from main import auth

from sqlalchemy import select,delete
from typing import List
from database.connection import get_session
from models.chat import Filters, MessageRequest

from function.tele_func import TelegramFunction
from telethon import events

filters = APIRouter(
    tags=["filters"]
)

@filters.get("/get_filter")
async def get_filter(session = Depends(get_session)):
    unique_filters = session.execute(select(Filters.filter_name).distinct())
    filters = [fil[0] for fil in unique_filters]
    return filters

@filters.get("/get_filter/{filter}")
async def get_filter(filter: str, session = Depends(get_session)):
    filter_groups = session.execute(select(Filters).where(Filters.filter_name == filter))
    result = filter_groups.scalars().all()
    if not result:
        raise HTTPException(status_code = 404, detail='해당 그룹이 존재하지 않습니다')
    return result

@filters.delete("/delete_filter/{filter}")
async def delete_filter(filter: str, session = Depends(get_session)):
    delete_groups = delete(Filters.where(Filters.filter_name == filter))
    session.execute(delete_groups)
    session.commit()
    return {"message": "filter deleted succesfully"}

@filters.post("/edit_filter")
async def update_filter(filters: Filters, session = Depends(get_session)):
    delete_filter = delete(Filters.where(Filters.filter_name == filter))
    session.execute(delete_filter)
    session.add_all(filters)
    session.commit()
    return {"message": "chat group updated succesfully"}

@filters.post("/send_message")
async def send_message(request: MessageRequest):
    try:
        message = await TelegramFunction.send_message(auth,request.chat_id,request.message)
        print(message.message)
        return {"message": f"{message.message}가 {message.peer_id} 로 전송"}
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))


@auth.on(events.NewMessage(chats=2149529921))
async def handler(event):
    print(f"새 메시지: {event.message.text}")
