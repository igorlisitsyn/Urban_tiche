from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
import asyncio
from const import API_TOKEN2
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from keyboard import *



bot = Bot(token=API_TOKEN2)

di = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weigth = State()



async def data():
    return 'Введите команду /start, чтобы начать общение.'

@di.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kbd)


@di.message_handler(text = 'Расcчитать')
async def inline_dutton(message: types.Message):
    await message.answer('Выберите опцию', reply_markup=markup)


@di.callback_query_handler(text = 'formulas')
async def formula(call: CallbackQuery):
    await call.message.reply(f'для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')

@di.callback_query_handler(text = 'calories')
async def start_user(call: CallbackQuery):
    await UserState.age.set()

    await call.message.reply('Введите свой возраст:')

@di.message_handler(state=UserState.age)
async def set_age(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['age'] = int(message.text)
    await UserState.next()
    await message.reply('Введите свой рост:')

@di.message_handler(state=UserState.growth)
async def set_growth(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['growth'] = float(message.text)
    await UserState.next()
    await message.reply('Введите свой вес:')

@di.message_handler(state=UserState.weigth)
async def set_weigth(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['weigth'] = float(message.text)

    async with state.proxy() as data:
        kalories = ( 10 * data['weigth'] + 6.25 * data['growth'] + 5 * data['age'] ) + 5
        await message.reply(f' Ваша норма калорий : {kalories}')

    await state.finish()

@di.message_handler()
async def all_massages(message: types.Message):

    dat = await data()
    await message.reply(dat)

if __name__ == '__main__':
    executor.start_polling(di, skip_updates=True)