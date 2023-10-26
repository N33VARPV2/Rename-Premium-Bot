import os
from dotenv import load_dotenv
load_dotenv()

# Mandatory variables for the bot to start

API_ID = int(os.getenv("API_ID", "11657778"))
API_HASH = os.environ.get("API_HASH", "56b209fe074993cf4d123fdfb74ab545")
TOKEN = os.environ.get("TOKEN", "6901673377:AAF4Ei4HStiRVjeMiT72Y9rV0vztLVbBoKs")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("5383602320")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DB_NAME = os.environ.get("DB_NAME", "Cluster0")
DB_URL = os.getenv("DB_URL", "mongodb+srv://vk3714414:vk3714414@cluster0.w7ztoys.mongodb.net/?retryWrites=true&w=majority") 
# OWNER_ID =  int(os.environ.get("OWNER_ID", "604152966")) 
# ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(5383602320)


#  Optionnal variables

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002138375005")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "MoviesDuniya4U") # For Force Subscription
# BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
# WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", 'https://telegra.ph/file/496e7ae942556eb072ab6.jpg') # image when someone hit /start # image when someone hit /start
# LINK_BYPASS = "False"
