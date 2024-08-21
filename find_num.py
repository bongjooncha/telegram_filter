import asyncio
import os
from dotenv import load_dotenv
from telethon.sync import TelegramClient

load_dotenv()

class TelegramForwarder:
    def __init__(self):
        self.api_id = os.getenv('telegram_id')
        self.api_hash = os.getenv('telegram_hash')
        self.phone_number = os.getenv('telegram_phone')
        self.client = TelegramClient('session_' + self.phone_number, self.api_id, self.api_hash)

    async def list_chats(self):
        await self.client.connect()

        # Ensure you're authorized
        if not await self.client.is_user_authorized():
            await self.client.send_code_request(self.phone_number)
            await self.client.sign_in(self.phone_number, input('Enter the code: '))

        # Get a list of all the dialogs (chats)
        dialogs = await self.client.get_dialogs()

        with open(f"chats_of_{self.phone_number}.txt", "w", encoding='utf-8') as chats_file:
            for dialog in dialogs:
                print(f"Chat ID: {dialog.id}, Title: {dialog.title}")
                chats_file.write(f"Chat ID: {dialog.id}, Title: {dialog.title} \n")
            

            print("List of groups printed successfully!")
    
async def main():
    forwarder = TelegramForwarder()
    await forwarder.list_chats()

if __name__ == "__main__":
    asyncio.run(main())