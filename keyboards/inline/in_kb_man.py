from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_main = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton(text='Показать наличие и описания', callback_data='show')],
    [
        InlineKeyboardButton(text='Добавить дату и описание', callback_data='add')
    ],[
        InlineKeyboardButton(text='Помощь', callback_data='help')
    ]
])