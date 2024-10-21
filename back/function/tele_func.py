from database.connection import get_session
from telethon import events


class TelegramFunction():
    async def read_chat_ids(auth):
        dialogs = await auth.get_dialogs()
        return dialogs
    
    async def send_message(auth, chat_id, message):
        send = await auth.send_message(chat_id,message)
        return send
    
    async def register_new_chat_handler(auth, tr:dict ,rrs: list, words: list):
        @auth.on(events.NewMessage(tr["id"]))
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
                    

    
    