import asyncio
from datetime import datetime

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