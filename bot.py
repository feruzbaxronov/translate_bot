import logging

import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "5035876028:AAEf-YtvyCpLY2oHBsSthXdK_dUWQwmyVRk"
wikipedia.set_lang("uz")

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
    await message.reply("wikibotga xush kelibsiz")



@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        respond=wikipedia.summary(massage.text)
        await massage.answer(respond)

    except:
        await massage.answer("Bu mavzuga oid hech nasra topilmadi")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)