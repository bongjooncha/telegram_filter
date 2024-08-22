import asyncio
from tel_func import TelegramForwarder
from datetime import datetime

async def send_hourly_message(forwarder, destination_channel_id):
    while True:
        now = datetime.now()
        # 정각 확인
        if now.minute == 0 and now.second == 0:
            await forwarder.client.send_message(destination_channel_id, "정상작동 중")
            print("정각 메시지 전송됨")
            # 60초 동안 대기하여 동일한 정각에서 메시지가 여러 번 전송되는 것을 방지
            await asyncio.sleep(60)
        await asyncio.sleep(1)  # 매 초마다 확인


async def main():
    forwarder = TelegramForwarder()
    await forwarder.client.connect()
    
    # 채널 갱신
    # await forwarder.list_chats()
    
    # #auth 확인
    if not await forwarder.client.is_user_authorized():
        await forwarder.client.send_code_request(forwarder.phone_number)
        await forwarder.client.sign_in(forwarder.phone_number, input('Enter the code: '))

    
    #메시지
    source_chat_id1=-1001379897604 #새우잡이어선
    last_message_id1 = None
    source_chat_id2=-1002149529921 #ㅇㅇ
    last_message_id2 = None
    source_chat_id3= 7438319188 #coinnews
    last_message_id3 = None
    destination_channel_id=-1002203481397 #ㄱㄴㄷ

    asyncio.create_task(send_hourly_message(forwarder, destination_channel_id))

    while True:
        last_message_id1 = await forwarder.forward_messages_to_channel(source_chat_id1, destination_channel_id, '', last_message_id1)
        last_message_id2 = await forwarder.forward_messages_to_channel(source_chat_id2, destination_channel_id, '', last_message_id2)
        last_message_id3 = await forwarder.forward_messages_to_channel(source_chat_id3, destination_channel_id, ['가능', 'asd', 'gdg'], last_message_id3)
        print(".")
        await asyncio.sleep(3)  # Adjust the delay time as needed
    # 전체 메시지 호출()
    # messages = await forwarder.fetch_all_messages(source_chat_ids,2)
    # for msg in messages:
    #     print(f"From Chat: {chat_ids.get(msg.chat_id)}")
    #     message_time = msg.date.strftime('%Y-%m-%d %H:%M:%S')
    #     print(f"Message Time: {message_time}")
    #     print(f"Message Content: {msg.text}")
    #     print("")




if __name__ == "__main__":
    asyncio.run(main())