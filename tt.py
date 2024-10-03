from function.tele_func import TelegramFunction
import asyncio

auth = TelegramFunction()

async def main():
    await auth.client.connect()
    dialogs = await auth.read_chat_ids()
    for dialog in dialogs:
        try:
            chat_id = dialog.entity.id
            chat_name = dialog.entity.title
            print(chat_id, chat_name)
        except AttributeError:
            pass

if __name__ == "__main__":
    asyncio.run(main())