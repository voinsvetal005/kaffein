import time
import logging
import asyncio

from aiogram import Bot, Dispatcher, executor, types

#bot = telebot.TeleBot('5973096764:AAHs4PL4fL-Y6mPJ1ObvgBtPJCwHib6mvL0')
# Адрес телеграм-канала, начинается с @
CHANNEL_NAME = '@xuinaizpodkonia'
CHANNEL_ID = '-1001565737707'

TOKEN = "5973096764:AAHs4PL4fL-Y6mPJ1ObvgBtPJCwHib6mvL0"
MSG = "Не спать!"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
chat_id = -1001565737707

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id} {user_full_name} {time.asctime()}')
    await message.reply(f"Привет, {user_full_name}!")

    for i in range(7):
        await asyncio.sleep(240)
        await bot.send_message(chat_id, MSG)

if __name__ == "__main__":
    executor.start_polling(dp)