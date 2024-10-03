from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.connection import conn
from function.tele_func import TelegramFunction

app = FastAPI()
app.middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

auth = TelegramFunction()

@app.on_event("startup")
def startup():
    conn()

@app.get("/synchronize_chat_ids")
async def synchronize_chat_ids():
    await auth.client.connect()
    dialogs = await auth.read_chat_ids()
    for dialog in dialogs:
        try:
            chat_id = dialog.entity.id
            chat_name = dialog.entity.title
            print(chat_id, chat_name)
        except AttributeError:
            pass


