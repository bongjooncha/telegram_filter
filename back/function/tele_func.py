from database.connection import get_session
from telethon import events

class TelegramFunction():
    async def read_chat_ids(auth):
        dialogs = await auth.get_dialogs()
        return dialogs
    
    async def send_message(auth, chat_id, message):
        send = await auth.send_message(chat_id,message)
        return send
    
    # def register_new_chat_handler(client,chat_id:int):
    #     @client.on(events.NewMessage(chat_id))
    #     async def handler(event):
    #         try: logger.in
    
    