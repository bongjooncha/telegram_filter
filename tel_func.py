import os
from dotenv import load_dotenv
from telethon.sync import TelegramClient
try:
    from chats_ids import chatIds
except ImportError:
    chatIds=0
    print("chats_id.py 없음")

load_dotenv()

class TelegramForwarder:
    def __init__(self):
        self.api_id = os.getenv('telegram_id')
        self.api_hash = os.getenv('telegram_hash')
        self.phone_number = os.getenv('telegram_phone')
        self.client = TelegramClient('session_' + self.phone_number, self.api_id, self.api_hash)
    # 채널불러오기
    async def list_chats(self):
        # Get a list of all the dialogs (chats)
        dialogs = await self.client.get_dialogs()

        chat_dict = {dialog.id: dialog.title for dialog in dialogs} 
        # Save the dictionary to a Python file
        with open("chats_ids.py", "w", encoding='utf-8') as chats_file:
            chats_file.write(f"chatIds = {chat_dict}\n")

        print("Dictionary of chat IDs and titles saved successfully!")
    
    #채팅 불러오기
    async def fetch_all_messages(self,chat_ids,n):
        all_messages = []
        for chat_id in chat_ids:
            async for message in self.client.iter_messages(chat_id, limit=n):
                all_messages.append(message)
        return all_messages

    #source: 불러오는 곳, destination: 목적지, 
    async def forward_messages_to_channel(self, source_chat_id, destination_channel_id, keywords, last_message_id):
        if last_message_id == None:
            last_message_id = (await self.client.get_messages(source_chat_id, limit=1))[0].id
        messages = await self.client.get_messages(source_chat_id, min_id=last_message_id, limit=None)
        new_last_message_id = last_message_id
        for message in reversed(messages):
            # Check if the message text includes any of the keywords
            if keywords:
                if message.text and any(keyword in message.text.lower() for keyword in keywords):
                    # Forward the message to the destination channel
                    sending = chatIds.get(message.chat_id) + ":\n" + message.text
                    await self.client.send_message(destination_channel_id, sending)

            else:
                    # Forward the message to the destination channel
                    sending = chatIds.get(message.chat_id) + ":\n" + message.text
                    await self.client.send_message(destination_channel_id, sending)
            new_last_message_id = max(new_last_message_id, message.id)


            # Update the last message ID
        return new_last_message_id
            

        
