import logging

from aiogram import Bot, Dispatcher, executor, types
from oxford import getDefinitions
from googletrans import Translator
translator=Translator()

API_TOKEN = '5005143255:AAGX75xcP-3FEAV7stkudhCcQV_ZjvKrZXU'


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Baxronov  Botiga Xush Kelibsiz\n Iltimos 2tadan ortiq so'z yuboring\n Ingliz yoki uzbek tilida")

@dp.message_handler()
async def tarjimon(message: types.Message):
    lang=translator.detect(message.text).lang
    if len(message.text.split())>2:
        dest='uz' if lang=='en' else 'en'
        await message.reply(translator.translate(message.text,dest).text)

  


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)