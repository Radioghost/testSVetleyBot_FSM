from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

ch_type_kb = ReplyKeyboardMarkup(
    keyboard=[[
      KeyboardButton('Белый белт'),
    KeyboardButton('Нить теплая'),
    KeyboardButton('Нить холодная')],
        [
    KeyboardButton('Прованс (малый разъем)')],[
    KeyboardButton('Прованс (большой разъем)')],[
    KeyboardButton('Занавес 2*6'),
    KeyboardButton('Занавес 3*3'),
    ],
    ], resize_keyboard=True, one_time_keyboard=True
)