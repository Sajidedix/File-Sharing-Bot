import os
import logging
from logging.handlers import RotatingFileHandler




BOT_TOKEN = os.environ.get("BOT_TOKEN", "7325029227:AAFTE1M7qVQpNATJh4wsuWxjCifVcvzdUJM")
API_ID = int(os.environ.get("API_ID", "10658015"))
API_HASH = os.environ.get("API_HASH", "a0087bca748f86698c53d291c9e5b3af")


OWNER_ID = int(os.environ.get("OWNER_ID", "6170962395"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://firstv142:tYCBfpwnFwVA2MHa@cluster0.h9thb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "Cluster0")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002256631540"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))


FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "600")) # auto delete in seconds


PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))



try:
    ADMINS=[6170962395]
    for x in (os.environ.get("ADMINS", "6170962395").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")









CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', "True") == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "❌𝘋𝘰𝘯'𝘵 𝘚𝘦𝘯𝘥 𝘔𝘦 𝘔𝘦𝘴𝘴𝘢𝘨𝘦𝘴 𝘋𝘪𝘳𝘦𝘤𝘵𝘭𝘺 𝘐'𝘮 𝘖𝘯𝘭𝘺 𝘍𝘪𝘭𝘦 𝘚𝘩𝘢𝘳𝘦 𝘉𝘰𝘵 !"

START_MSG = os.environ.get("START_MESSAGE", "Hᴇʟʟᴏ {mention} Bᴀʙᴜ\n\nI Cᴀɴ Sᴛᴏʀᴇ Pʀɪᴠᴀᴛᴇ Fɪʟᴇs Iɴ Sᴘᴇᴄɪғɪᴇᴅ Cʜᴀɴɴᴇʟ Aɴᴅ Oᴛʜᴇʀ Usᴇʀs Cᴀɴ Aᴄᴄᴇss Iᴛ Fʀᴏᴍ Sᴘᴇᴄɪᴀʟ Lɪɴᴋ.")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {mention}\n\n<b>You Need To Join In My Channel/Group To Use Me\n\nKindly Please Join Channel</b>")





ADMINS.append(OWNER_ID)
ADMINS.append(6170962395)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
