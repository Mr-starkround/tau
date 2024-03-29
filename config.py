# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

import logging
import os
from distutils.util import strtobool
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6770397722:AAFVZ3Y0Usru6yAfHJ376dqEiQk1AyfQ-lk")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "20913084"))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "67eb42c8167df3ebe8935e961e3349e5")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002093164388"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "OnlyVaan")

# Heroku Credentials for updater.
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

# Database
DB_URI = os.environ.get("DATABASE_URL", "postgres://uwkjnfhs:lUpqrKIiU6GOiZol1tP7T0R3ehKK9GP5@rain.db.elephantsql.com/uwkjnfhs")

# Protect Content
PROTECT_CONTENT = strtobool(os.environ.get("PROTECT_CONTENT", "True"))

# Username CH & Group
CHANNEL = os.environ.get("CHANNEL", "Jawafes")
GROUP = os.environ.get("GROUP", "jawa_grup")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_1 = int(os.environ.get("FORCE_SUB_1", "-1001992270770"))
FORCE_SUB_2 = int(os.environ.get("FORCE_SUB_2", "-1001957222400"))
FORCE_SUB_3 = int(os.environ.get("FORCE_SUB_3", "-1002074892874"))
FORCE_SUB_4 = int(os.environ.get("FORCE_SUB_4", "-1002087560839"))
FORCE_SUB_5 = int(os.environ.get("FORCE_SUB_5", "0"))
FORCE_SUB_6 = int(os.environ.get("FORCE_SUB_6", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hallo {first}</b>\n\n<b>✨Silahkan join grup dan channel di bawah ini untuk bisa mengakses video.\n Hubungi @OnlyVaan jika ada masalah dengan bot.</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "1228099043").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hallo {first}</b>\n\n<b>✨Silahkan join grup dan channel di bawah ini untuk bisa mengakses video.\n Hubungi @OnlyVaan jika ada masalah dengan bot.</b>",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == "True"

ADMINS.extend(())


LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
