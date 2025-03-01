import json
from datetime import datetime
from pyrogram import Client, filters
from ftm import Config  # Extracting values from ftm.py

# Load user data
try:
    with open("user_data.json", "r") as f:
        user_data = json.load(f)
except FileNotFoundError:
    user_data = {}

# Save user data
def save_data():
    with open("user_data.json", "w") as f:
        json.dump(user_data, f, indent=4)

# Check premium status
def is_premium(user_id):
    return user_data.get(str(user_id), {}).get("premium", False)

# Check and update download limit
def check_download_limit(user_id):
    today = datetime.now().strftime("%Y-%m-%d")

    if str(user_id) not in user_data:
        user_data[str(user_id)] = {"premium": False, "date": today, "count": 0}

    if user_data[str(user_id)]["date"] != today:
        user_data[str(user_id)] = {"premium": user_data[str(user_id)]["premium"], "date": today, "count": 0}

    if user_data[str(user_id)]["premium"] or user_data[str(user_id)]["count"] < 20:
        user_data[str(user_id)]["count"] += 1
        save_data()
        return True

    return False

# Premium commands
@Client.on_message(filters.command("premium"))
async def premium_info(client, message):
    await message.reply("💎 **Premium Plans:**\n- Unlimited Downloads\n- Faster Processing\n\nUse `/myplan` to check your status.")

@Client.on_message(filters.command("myplan"))
async def my_plan(client, message):
    user_id = message.from_user.id
    if is_premium(user_id):
        await message.reply("✅ **You are a Premium User!**\nUnlimited downloads available.")
    else:
        await message.reply("⚠️ **You are on the Free Plan**\nLimit: 20 downloads per day.")

@Client.on_message(filters.command("remove_premium"))
async def remove_premium(client, message):
    user_id = message.from_user.id
    if is_premium(user_id):
        user_data[str(user_id)]["premium"] = False
        save_data()
        await message.reply("❌ **Premium Removed**. You are now on the free plan.")
    else:
        await message.reply("⚠️ You are not a premium user.")

@Client.on_message(filters.command("add_premium"))
async def add_premium(client, message):
    if message.from_user.id != OWNER_ID:
        await message.reply("❌ **You are not authorized to add premium users.**")
        return

    if len(message.command) < 2:
        await message.reply("⚠️ **Usage:** `/add_premium <user_id>`\nExample: `/add_premium 987654321`")
        return

    user_id = message.command[1]

    if user_id in user_data:
        user_data[user_id]["premium"] = True
        save_data()
        await message.reply(f"✅ **User {user_id} has been upgraded to Premium!**\n\n{DEV_CREDIT}", disable_web_page_preview=True)
    else:
        user_data[user_id] = {"premium": True, "date": datetime.now().strftime("%Y-%m-%d"), "count": 0}
        save_data()
        await message.reply(f"✅ **User {user_id} has been added as a Premium User!**\n\n{DEV_CREDIT}", disable_web_page_preview=True)
