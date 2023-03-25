from pyrogram import Client, filters
from pyrogram.types import Message


# It's really highly recommended to write handlers like this. Just do it async already!
@Client.on_message(filters.incoming)
async def example_handler(client: Client, msg: Message):
    await msg.reply_text("Hello, I'm example from https://github.com/ANoneTypeOn/BotBase")
    await client.get_me()
