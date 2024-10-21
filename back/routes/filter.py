from fastapi import APIRouter,  Depends, HTTPException
from main import client

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
    unique_filters = session.execute(select(Filters.filter_name, Filters.on_off))
    filters = [{"filter_name": fil[0], "on_off": fil[1]} for fil in unique_filters]
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
    delete_groups = delete(Filters).where(Filters.filter_name == filter)
    session.execute(delete_groups)
    session.commit()
    return {"message": "filter deleted succesfully"}

@filters.post("/edit_filter")
async def update_filter(filters: Filters, session = Depends(get_session)):
    delete_filter = delete(Filters).where(Filters.filter_name ==  filters.filter_name)
    session.execute(delete_filter)
    session.add(filters)
    session.commit()
    return {"message": "filter updated succesfully"}


@filters.post("/send_message")
async def send_message(request: MessageRequest):
    try:
        message = await TelegramFunction.send_message(client,request.chat_id,request.message)
        print(message.message)
        return {"message": f"{message.message}가 {message.peer_id} 로 전송"}
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))


@filters.post("/register_chat")
async def register_chat(chat_request: Filters):
    for tr in chat_request.tr_id_name:
        await TelegramFunction.register_new_chat_handler(client, tr, chat_request.rr_id_name, chat_request.words)
