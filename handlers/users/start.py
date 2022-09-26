from aiogram import types
from loader import dp

from keyboards.inline import ikb_main

@dp.message_handler(text='/start')
async def command_start(msg: types.Message):
    await msg.answer(f'Привет {msg.from_user.full_name} \n'
                     f' Ты общаешся с  [TEST]Svetley\n'
                     f' Вот что он умеет делать', reply_markup=ikb_main
                     )