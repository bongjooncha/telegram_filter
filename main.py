import asyncio
from tel_func import TelegramForwarder
import time
try:
    from chats_ids import chatIds
except ImportError:
    exit()

async def process_chat(forwarder, chat_id, destination_channel_id, keywords, last_message_id):
    try:
        return await forwarder.forward_messages_to_channel(chat_id, destination_channel_id, keywords, last_message_id)
    except ValueError as e:
        await forwarder.client.send_message(destination_channel_id, "텔레그램 오류 재시작")
        await forwarder.send_error_message(destination_channel_id, str(e))
        return last_message_id

async def main():
    forwarder = TelegramForwarder()
    await forwarder.client.connect()
    
    
    # #auth 확인
    if not await forwarder.client.is_user_authorized():
        await forwarder.client.send_code_request(forwarder.phone_number)
        await forwarder.client.sign_in(forwarder.phone_number, input('Enter the code: '))

    
    #메시지
    chat_ids_list = list(chatIds.keys())
    last_message_id = [None]*len(chatIds)
    destination_channel_id = -1002158655628
    await forwarder.client.send_message(destination_channel_id, "시작")
    print("시작")

    while True:
            start_time = time.time()
            tasks = [
                process_chat(forwarder, chat_id, destination_channel_id, ['실리콘투','화장품','뷰티'], last_message_id[i])
                for i, chat_id in enumerate(chat_ids_list) if chat_id != destination_channel_id
            ]
            results = await asyncio.gather(*tasks)
            for i, result in enumerate(results):
                last_message_id[i] = result
            
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"실행 시간: {execution_time:.2f}초")
            await forwarder.client.send_message(destination_channel_id, f"실행 시간: {execution_time:.2f}초")
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