import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "2535079"))
  API_HASH = os.environ.get("API_HASH", "e7e40943947d17e07469260d265a26cd")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "6369560123:AAE38y26FV4_yl1SEHqPvmu0-_L18KNecQE")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "MRG_db_bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001755291047"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "gplinks.in")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "a001f696ef0e09d9134e95d8a3b71ad1c4e6b177")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "674591941"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://moviezworld:wrecOMCguqhpz3ER@cluster0.jj7fovh.mongodb.net/?retryWrites=true&w=majority")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001616124107")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001988838005"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [MRG Storage](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [Yrus](https://telegram.me/MRGOfficial_admin)
 
 I am Super Movies Uploader Support My Hard Work.

[Donate Me]()
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.
"""
