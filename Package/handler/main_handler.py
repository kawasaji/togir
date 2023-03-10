from aiogram import *
from aiogram import types
import sys

sys.path.insert(1, 'Package/services')
sys.path.insert(1, 'Package')

from main import *

@dp.message_handler(commands=['start'], commands_prefix='!/.')
async def start(message: types.Message):
    await message.reply("привет")
    if (
        message.chat.type in ("group", "supergroup")
        and not BotDB.chat_exists(chat_id=message.chat.id)
    ):
        BotDB.add_chat(message.chat.id)
