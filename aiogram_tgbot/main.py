import logging

from aiogram import Bot, Dispatcher, types
from os import getenv
from sys import exit
from aiogram.utils import executor


bot_token = getenv("BOT_TOKEN")
if not bot_token:
    exit("Error: no token provider")
    
# Bot object
bot = Bot(token=bot_token)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands="start")
async def start_function(message: types.Message):
    await message.answer("Привет!\nМеня зовут Стасик. Я помогу тебе в изучении Python присылая задачки разной "
                         "сложности.\nИ первый вопрос к тебе, как тебя зовут?")

    #await message.reply("Hi")


executor.start_polling(dp, skip_updates=True)