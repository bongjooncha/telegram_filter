import asyncio
from config import Config

async def main():
    client = Config.CLIENT_NAME
    await client.connect()
    
    # #auth 확인
    if not await client.is_user_authorized():
        await client.send_code_request(Config.TELEGRAM_PHONE)
        await client.sign_in(Config.TELEGRAM_PHONE, input('Enter the code: '))


if __name__ == "__main__":
    asyncio.run(main())
