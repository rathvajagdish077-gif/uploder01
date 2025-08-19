#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "28562158"))
API_HASH = environ.get("API_HASH","62c1363a1b4ae6cdcd8328e6a0f1e08c")
BOT_TOKEN = environ.get("BOT_TOKEN", "7392798055:AAFVnDTVzaylEjQxpPLSipQ6g7DrFRl1x3Y")

OWNER = int(environ.get("OWNER", "7447651332"))
CREDIT = environ.get("CREDIT", "𓍯𝙎𝙪𝙟𝙖𝙡⚝")

TOTAL_USER = os.environ.get('TOTAL_USERS', '7447651332').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '7447651332').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
