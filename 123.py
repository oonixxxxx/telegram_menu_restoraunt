import logging
import aiogram
from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = '6099085169:AAHLDVW8Yx9aLHurzC8vhrHEkcUxYTHUBe0'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

busket = []

dict = {'burger': 500,
        'coffee': 100}

def get_cost(item):
    return dict[str(item)]

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer(f"Hi!\nМеню:\n {dict}")


@dp.message_handler(commands=['pay'])
async def pay_busket(message: types.Message):
    await message.answer(f'{busket}Стоимость:{summary_cost} \n Выбирете способ оплаты')

@dp.message_handler()
async def add_to_busket(message: types.Message):
    global summary_cost
    if message.text in dict:
        busket.append(message.text)
    print(message.text)
    print(dict[message.text])
    summary_cost = summary_cost + int(dict(message.text))


if __name__ == '__main__':
    executor.start_polling(dp)