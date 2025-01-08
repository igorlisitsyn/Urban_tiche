from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
import asyncio
from const import API_TOKEN



bot = Bot(token=API_TOKEN)

bispatcher = Dispatcher(bot, storage=MemoryStorage())

async def data():
    return 'Введите команду /start, чтобы начать общение.'

@bispatcher.message_handler(commands=['start'])
async def start(message):
    await message.reply('Привет! Я бот помогающий твоему здоровью.')
    #print('Привет! Я бот помогающий твоему здоровью.')

@bispatcher.message_handler()
async def all_massages(message: types.Message):
    #print('Введите команду /start, чтобы начать общение.')
    dat = await data()
    await message.reply(dat)

if __name__ == '__main__':
    executor.start_polling(bispatcher, skip_updates=True)