from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


kbd = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Расcчитать'),
            # KeyboardButton(text='Информация'),
        ],
    ],
    resize_keyboard=True
)


markup = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
            InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas'),
        ],
    ],
)