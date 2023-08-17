from telethon import TelegramClient
from telethon.sessions import StringSession


API_KEY = int(input("21590558"))
API_HASH = input("9767814b790f12ad9a333a20bcaf1200") 


bot = TelegramClient(StringSession(), API_KEY, API_HASH)
bot.start()
string_session = bot.session.save()
print(string_session)
