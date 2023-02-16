import openai
import logging
from aiogram import Bot, Dispatcher, executor, types

openai.api_key = 'API KEY'
TOKEN = "TOKEN"

# Configure logging
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Чтобы задать вопрос напишите.")


@dp.message_handler()
async def send(message: types.Message):
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=message.text,
        temperature=0.5,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
    )
    await message.reply(text=response['choices'][0]['text'])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
