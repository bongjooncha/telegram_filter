from fastapi import APIRouter,  Depends, HTTPException

from sqlalchemy import select,delete
from typing import List
from database.connection import get_session
from models.chat import ChatGroups

group = APIRouter(
    tags=["groups"]
)


@group.get("/get_group_names")
async def get_all_group_names(session=Depends(get_session)):
    unique_groups = session.execute(select(ChatGroups.group).distinct())
    groups = [group[0] for group in unique_groups]
    return groups

@group.get("/get_chat_group/{group}")
async def get_chat_group(group: str, session=Depends(get_session)):
    chat_groups = session.execute(select(ChatGroups).where(ChatGroups.group == group))
    result = chat_groups.scalars().all()
    if not result:
        raise HTTPException(status_code = 404, detail='해당 그룹이 존재하지 않습니다')
    return result

@group.delete("/delete_chat_group/{group}")
async def delete_chat_group(group: str, session=Depends(get_session)):
    delete_stmt = delete(ChatGroups).where(ChatGroups.group == group)
    session.execute(delete_stmt)
    session.commit()
    return {"message": "chat group deleted succesfully"}

@group.post("/edit_chat_group")
async def update_chat_groups(chat_groups: List[ChatGroups], session=Depends(get_session)):
    group_value = chat_groups[0].group
    delete_stmt = delete(ChatGroups).where(ChatGroups.group == group_value)
    session.execute(delete_stmt)
    session.add_all(chat_groups)
    session.commit()
    return {"message": "chat group updated succesfully"}
