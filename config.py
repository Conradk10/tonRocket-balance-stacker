import sys

API_ID = 2040
API_HASH = "b18441a1ff607e10a989891a5462e627"
DEVICE_MODEL = "PC 64bit"
SYSTEM_VERSION = "Windows 10"
APP_VERSION = "4.6"
LANG_CODE = "ru"
SYSTEM_LANG_CODE = "ru-RU"

SESSIONS_DIR = "sessions"  # Не менять

BOT_USERNAME = "@tonRocketBot".replace("@", "")

try:
    OWNER_USERNAME = sys.argv[1]
except IndexError:
    OWNER_USERNAME = input('Укажите юзернейм владельца (Пример: @ca4tuk): ')
