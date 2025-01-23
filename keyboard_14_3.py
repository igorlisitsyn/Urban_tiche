from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


kbd = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Расcчитать'),
            # KeyboardButton(text='Информация'),
        ],
        [
            KeyboardButton(text='Купить'),
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

change_kb = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text='Product1', callback_data='product_buying'),
            InlineKeyboardButton(text='Product2', callback_data='product_buying'),
            InlineKeyboardButton(text='Product2', callback_data='product_buying'),
            InlineKeyboardButton(text='Product2', callback_data='product_buying'),
        ],
    ],
)