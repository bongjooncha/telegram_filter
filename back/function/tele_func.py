import config
from database.connection import get_session

class TelegramFunction:
    client = config.Config.CLIENT_NAME

    async def read_chat_ids(self):
        dialogs = await self.client.get_dialogs()
        return dialogs

