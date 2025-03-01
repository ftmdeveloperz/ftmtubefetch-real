from pyrogram import Client, filters
from ftm import Config  # Import from root directory
import premium  # Import premium features
import clone  # Import bot cloning

# Create a Pyrogram client
app = Client(
    "my_bot",
    api_id=Config.API_ID, 
    api_hash=Config.API_HASH, 
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="Youtube")  # Keep this if your plugins are in "Youtube" folder
)

# Start the bot
print(f"🎊 🎊 I AM ALIVE 🎊 & Powered by Fᴛᴍ Dᴇᴠᴇʟᴏᴘᴇʀᴢ 🚀\n👑 Owner ID: {Config.OWNER_ID}")

app.run()
