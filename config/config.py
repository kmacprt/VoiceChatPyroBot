# Just copy this file to config.py and change it to your info.
from pyrogram import filters

# Get these two from https://my.telegram.org
API_ID = 1733305
API_HASH = "f423cffca6b5b7247b31b5b0df61f48d"

# Get this from @Botfather
TOKEN = "1559250481:AAGq42N3_6e-a2AZ3M4M-5nj3WrT1NK4QzA"

# Your MongoDB URI (using a database named "vcpb"), if you don't provide, you can't use the playlist feature and wont see now playing message
MONGO_DB_URI = "mongodb://vcpb:dkkaj0123456@mongodb/vcpb?replicaSet=rs0"

# The IDs of the users which can stream, skip, pause and change volume
SUDO_USERS = [
     1156597097
]

# The ID of the group where your bot streams
GROUP = -1001390893086

# Users must join the group before using the bot (note: the bot should be admin in the group if you enable this)
USERS_MUST_JOIN = False

# Choose the preferred language for your bot. If English leave as it is, or change to the code of any supported language.
LANG = "en"

# Max video duration allowed for user downloads in minutes
DUR_LIMIT = 30

# No need to touch the following.
LOG_GROUP = GROUP if MONGO_DB_URI != "" else None
SUDO_FILTER = filters.user(SUDO_USERS)
