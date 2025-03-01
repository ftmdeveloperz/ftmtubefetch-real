import os
import subprocess
from pyrogram import Client, filters
from ftm import GITHUB_REPO, DEV_CREDIT  # Extracting values from ftm.py

@Client.on_message(filters.command("clonebot"))
async def clone_bot(client, message):
    await message.reply("🔄 **Bot Cloning Started** 🔄\n\nSend your **Bot Token** to create a new bot.")

    @Client.on_message(filters.text)
    async def get_token(client, msg):
        bot_token = msg.text.strip()

        if not bot_token.startswith("5") or len(bot_token) < 40:
            await msg.reply("⚠️ Invalid **Bot Token**. Please provide a correct one.")
            return

        await msg.reply("🛠 **Creating Your Bot... Please Wait!**")

        # Create a new bot directory
        new_bot_dir = f"bot_{bot_token[:10]}"
        os.makedirs(new_bot_dir, exist_ok=True)

        # Clone the GitHub repo
        subprocess.run(f"git clone {GITHUB_REPO} {new_bot_dir}", shell=True)

        # Replace the bot token in ftm.py
        config_path = os.path.join(new_bot_dir, "ftm.py")
        with open(config_path, "w") as config_file:
            config_file.write(f'API_ID = "your_api_id"\nAPI_HASH = "your_api_hash"\nBOT_TOKEN = "{bot_token}"\n')

        # Send deployment instructions
        await msg.reply(
            f"✅ **Your bot has been successfully cloned!**\n\n"
            f"🔹 **Deployment Instructions:**\n"
            f"1. Go to `{new_bot_dir}`\n"
            f"2. Run: `python ftm_tubefetch.py`\n\n"
            f"{DEV_CREDIT}"
        )
