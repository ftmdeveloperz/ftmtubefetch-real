from pyrogram import Client, filters
import os
import premium  # Import premium features
import clone  # Import bot cloning

# Dynamically import everything from ftm.py
from Youtube import ftm  

# Create a Pyrogram client
app = Client(
    "my_bot",
    api_id=ftm.API_ID, 
    api_hash=ftm.API_HASH, 
    bot_token=ftm.BOT_TOKEN,
    plugins=dict(root="Youtube")
)

# Start the bot
print("🎊 🎊 I AM ALIVE 🎊 & Powered by Fᴛᴍ Dᴇᴠᴇʟᴏᴘᴇʀᴢ 🚀")

PORT = int(os.environ.get("PORT", 8080))
app.run(port=PORT)
