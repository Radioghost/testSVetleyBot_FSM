from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

show_again_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
      KeyboardButton('Выбрать другое'),
    KeyboardButton('В начало'),
    ]]
    , resize_keyboard=True, one_time_keyboard=True
)