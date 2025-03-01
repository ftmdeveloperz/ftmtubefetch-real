###ftm.py
import os

class Config(object):
    # Required Bot Credentials
    API_ID = int(os.getenv("API_ID", 22141398))
    API_HASH = os.getenv("API_HASH", '0c8f8bd171e05e42d6f6e5a6f4305389')
    BOT_TOKEN = os.getenv("BOT_TOKEN", '8105194942:AAFzL74g4y3EMJdouoVUtRig4SP_1eZk_xs')

    # Owner Settings
    OWNER_ID = int(os.getenv("OWNER_ID", "7744665378"))  # Replace with your ID

    # Force Subscription Channel ID
    CHANNEL = os.getenv("CHANNEL", "-1002369984275")  # Your channel ID for force join

    # Cloning & Repo Information
    GITHUB_REPO = "https://github.com/ftmdeveloperz/FtmTubeFetch"
    DEV_CREDIT = "👨‍💻 **Developer:** [Fᴛᴍ Dᴇᴠᴇʟᴏᴘᴇʀᴢ](https://t.me/ftmdeveloperz) | [GitHub](https://github.com/ftmdeveloperz) | [YouTube](https://youtube.com/@ftmdeveloperz)\n" \
                 "🔹 **Credits:** [ftmdeveloperz](https://t.me/ftmdeveloperz) | [GitHub](https://github.com/ftmdeveloperz) | [YouTube](https://youtube.com/@ftmdeveloperz)\n" \
                 "🔹 [ftmbotzx](https://t.me/ftmbotzx) | [GitHub](https://github.com/ftmbotzx) | [YouTube](https://youtube.com/@ftmbotzx) | [Channel](https://t.me/ftmbotzx)\n" \
                 "🔹 [Support](https://t.me/ftmbotzx_support) | [YouTube](https://youtube.com/@ftmbotzx_support)"
