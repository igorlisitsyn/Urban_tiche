from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
import asyncio
from const import API_TOKEN



bot = Bot(token=API_TOKEN)

bispatcher = Dispatcher(bot, storage=MemoryStorage())



@bispatcher.message_handler(commands=['start'])
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.')

@bispatcher.message_handler()
async def all_massages(message):
    print('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(bispatcher, skip_updates=True)