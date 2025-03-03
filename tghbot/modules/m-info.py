import os
import subprocess
from pyrogram import Client, filters
from pyrogram.types import Message

# Initialize the bot
app = Client("bot")

# Command handler to get media info
@app.on_message(filters.command("mediainfo") & filters.private)
async def media_info(client, message: Message):
    try:
        if not message.reply_to_message or not message.reply_to_message.media:
            await message.reply_text("Please reply to a media message.")
            return

        file_path = await client.download_media(message.reply_to_message)
        result = subprocess.run(["mediainfo", file_path], stdout=subprocess.PIPE)
        await message.reply_text(result.stdout.decode())
        os.remove(file_path)
    except Exception as e:
        await message.reply_text(f"An error occurred: {e}")

# Run the bot
app.run()
