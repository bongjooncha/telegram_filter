import asyncio
from function.tele_func import TelegramFunction

async def main():
    client = TelegramFunction().client
    await client.connect()
    
    # #auth 확인
    if not await client.is_user_authorized():
        await client.send_code_request(TelegramFunction().phone_number)
        await client.sign_in(TelegramFunction().phone_number, input('Enter the code: '))


if __name__ == "__main__":
    asyncio.run(main())
