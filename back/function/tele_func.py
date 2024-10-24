from fastapi import Depends
from database.connection import get_session
from telethon import events
from models.chat import Filters
from sqlalchemy import select


class TelegramFunction():
    def __init__(self):
        self.handlers = []

    # 체팅 조회(채팅 이름, 채팅 id 출력)
    async def read_chat_ids(auth):
        dialogs = await auth.get_dialogs()
        return dialogs    
    
    # 메세지 전송(채팅 id, 메세지 입력, 텔레그램으로 메시지 출력)
    async def send_message(auth, chat_id, message):
        send = await auth.send_message(chat_id,message)
        return send

    # 필터 핸들러 생성(받은 문자열 필터링 후 전송)
    def create_handler(self, auth, tr:dict ,rrs: list, words: list):
        async def handler(event):
            if len(words) != 0:
                if event.message.text and any(word in event.message.text.lower() for word in words):
                    for rr in rrs:
                        message = tr["name"] + ":\n" + event.message.text
                        await auth.send_message(rr["id"], message)
            else:
                for rr in rrs:
                    message = tr["name"] + ":\n" + event.message.text
                    await auth.send_message(rr["id"], message)
        return handler
    
    # 핸들러 등록(필터 정보 입력, 핸들러 생성)
    async def register_handler(self, auth, tr:dict ,rrs: list, words: list):
        handler  = auth.on(events.NewMessage(tr["id"]))(self.create_handler(auth, tr, rrs, words))
        self.handlers.append(handler)

    # 핸들러 재시작
    async def restart_handler(self, auth, session):
        for handler in self.handlers:
            auth.remove_event_handler(handler)
        self.handlers.clear()
        await self.run_on_filters(auth, session)

    # on필터 확인후 전부 실행
    async def run_on_filters(self, auth, session):
        filters = session.execute(select(Filters).where(Filters.on_off == True))
        filters = filters.scalars().all()
        for filter in filters:
            for tr in filter.tr_id_name:
                try:
                    await self.register_handler(auth, tr, filter.rr_id_name, filter.words)
                except Exception as e:
                    print(e)
        return filters


