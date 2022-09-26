from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

yn_kb = ReplyKeyboardMarkup(
    keyboard=[
			[
      		KeyboardButton('Да'),
    		KeyboardButton('Нет'),
    		]
    		], resize_keyboard=True, one_time_keyboard=True
)
