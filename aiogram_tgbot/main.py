import logging

from aiogram import Bot, Dispatcher, types
from os import getenv
from sys import exit
from aiogram.utils import executor

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from StepStates import StepStates
from messages import MESSAGES

bot_token = getenv("BOT_TOKEN")
if not bot_token:
    exit("Error: no token provider")

# Bot object
bot = Bot(token=bot_token)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands="start")
async def start_function(message: types.Message):
    await message.answer(MESSAGES['start'], reply=False)


@dp.message_handler(state=StepStates.AGE_STATE)
async def get_name(message: types.Message):
    name = message.text
    await message.answer(MESSAGES['get_age'])


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


executor.start_polling(dp, skip_updates=True)
