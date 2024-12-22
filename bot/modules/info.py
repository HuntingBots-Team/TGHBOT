from nekozee import Client
# created by HuntingBots 
# Initialize the Pyrogram client
app = Client("bot")

@app.on_message()
async def user_info(client, message):
    user = message.from_user

    if user:
        user_details = (
            f"User Info:\n"
            f"ID: {user.id}\n"
            f"Username: {user.username}\n"
            f"First Name: {user.first_name}\n"
            f"Last Name: {user.last_name}\n"
            f"Language Code: {user.language_code}\n"
            f"Is Bot: {user.is_bot}\n"
        )
        await message.reply(user_details)
    else:
        await message.reply("No user info available.")

@app.on_message()
async def chat_info(client, message):
    chat = message.chat

    chat_details = (
        f"Chat Info:\n"
        f"ID: {chat.id}\n"
        f"Title: {chat.title}\n"
        f"Username: {chat.username}\n"
        f"Type: {chat.type}\n"
    )
    await message.reply(chat_details)

if __name__ == "__main__":
    app.run()
