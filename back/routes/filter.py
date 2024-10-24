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

# 필터 조회(필터 이름, 필터 켜짐 여부)
@filters.get("/get_filter")
async def get_filter(session = Depends(get_session)):
    unique_filters = session.execute(select(Filters.filter_name, Filters.on_off))
    filters = [{"filter_name": fil[0], "on_off": fil[1]} for fil in unique_filters]
    return filters

# 필터 조회(개별 필터의 정보)
@filters.get("/get_filter/{filter}")
async def get_filter(filter: str, session = Depends(get_session)):
    filter_groups = session.execute(select(Filters).where(Filters.filter_name == filter))
    result = filter_groups.scalars().all()
    if not result:
        raise HTTPException(status_code = 404, detail='해당 그룹이 존재하지 않습니다')
    return result

# 개별 필터 삭제
@filters.delete("/delete_filter/{filter}")
async def delete_filter(filter: str, session = Depends(get_session)):
    delete_groups = delete(Filters).where(Filters.filter_name == filter)
    session.execute(delete_groups)
    session.commit()
    return {"message": "filter deleted succesfully"}

# 필터 수정
@filters.post("/edit_filter")
async def update_filter(filters: Filters, session = Depends(get_session)):
    delete_filter = delete(Filters).where(Filters.filter_name ==  filters.filter_name)
    session.execute(delete_filter)
    session.add(filters)
    session.commit()
    return {"message": "filter updated succesfully"}

# 메시지 전송(비사용중)
@filters.post("/send_message")
async def send_message(request: MessageRequest):
    try:
        message = await TelegramFunction.send_message(client,request.chat_id,request.message)
        return {"message": f"{message.message}가 {message.peer_id} 로 전송"}
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))

# on 필터 전부 실행
@filters.get("/run_all_on")
async def run_all_on(session = Depends(get_session)):
    telegram_function = TelegramFunction()
    result = await telegram_function.restart_handler(auth = client,session = session)
    return result
