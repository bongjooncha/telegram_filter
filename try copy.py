try:
    from chats_ids import chatIds
except ImportError:
    exit()

chat_ids_list = list(chatIds.keys())
print(chat_ids_list)