from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
import asyncio
from const import API_TOKEN2
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


from keyboard_14_4 import *
from produkt_db import *


bot = Bot(token=API_TOKEN2)

di = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weigth = State()

pik =  'https://images.prom.ua/4327787646_w700_h500_spirulina-spirul-dlya.jpg'
pik2 = 'https://img5.lalafo.com/i/posters/original/b2/04/cc/43763d5b5c0b5a2e7f05d6e8e5.jpeg'
pik3 = 'https://i.pinimg.com/originals/b0/54/28/b0542877d0ce131fe13038aab8f92237.png'
pik4 = 'http://cdn01.ru/files/users/images/48/1e/481e523f4648d0b604ecf3e053f0cb9a.jpg'

picture = [pik, pik2, pik3, pik4]
async def data():
    return 'Введите команду /start, чтобы начать общение.'

@di.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kbd)

@di.message_handler(text = 'Купить')
async def get_buying_list(message: types.Message):
    chat_id = message.from_user.id
    produkt = get_all_products()
    index = 0
    # await message.answer('Название: Product 1 | Описание: описание 1 | Цена: <number * 100')
    # await di.bot.send_photo(chat_id=chat_id, photo=pik)
    # await message.answer('Название: Product 2 | Описание: описание 2 | Цена: <number * 200')
    # await di.bot.send_photo(chat_id=chat_id, photo=pik2)
    # await message.answer('Название: Product 3 | Описание: описание 3 | Цена: <number * 300')
    # await di.bot.send_photo(chat_id=chat_id, photo=pik3)
    # await message.answer('Название: Product 4 | Описание: описание 4 | Цена: <number * 400')
    # await di.bot.send_photo(chat_id=chat_id, photo=pik4)
    for prod in produkt:

        await message.answer(f'Название: {prod[1]} | Описание: {prod[2]} | Цена: {prod[3]}')
        await di.bot.send_photo(chat_id=chat_id, photo=picture[index])
        index += 1
    await message.answer('Выберите продукт для покупки:', reply_markup=change_kb)



@di.message_handler(text = 'Расcчитать')
async def inline_dutton(message: types.Message):
    await message.answer('Выберите опцию', reply_markup=markup)


@di.callback_query_handler(text = 'product_buying')
async def formula(call: CallbackQuery):
    await call.message.reply(f'Вы успешно приобрели продукт!')


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