import asyncio
from tel_func import TelegramForwarder
from datetime import datetime
try:
    from chats_ids import chatIds
except ImportError:
    exit()

async def send_hourly_message(forwarder, destination_channel_id):
    while True:
        now = datetime.now()
        # 정각 확인
        if now.hour == 12 and now.minute == 0 and now.second == 0:
            await forwarder.client.send_message(destination_channel_id, "정상작동 중")
            print("정각 메시지 전송됨")
            # 60초 동안 대기하여 동일한 정각에서 메시지가 여러 번 전송되는 것을 방지
            await asyncio.sleep(60)
        await asyncio.sleep(60)  # 매 초마다 확인


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
    chat_ids_list = list(chatIds.keys())
    last_message_id = [None]*len(chatIds)
    destination_channel_id = -1002158655628
    await forwarder.client.send_message(destination_channel_id, "시작")
    asyncio.create_task(send_hourly_message(forwarder, destination_channel_id))

    while True:
        for i in range(len(chatIds)):
            if chat_ids_list[i] != destination_channel_id:
                try:
                    last_message_id[i] = await forwarder.forward_messages_to_channel(chat_ids_list[i],
                                                                                 destination_channel_id, 
                                                                             ['실리콘투','화장품','뷰티'], 
                                                                                 last_message_id[i])
                except ValueError as e:
                    await forwarder.client.send_message(destination_channel_id, "텔레그램 오류 재시작")
                    await forwarder.send_error_message(destination_channel_id,str(e))
        print(1)
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