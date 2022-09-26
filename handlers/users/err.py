from aiogram import types
from loader import dp

@dp.message_handler()
async def command_err(msg: types.Message):
    await msg.answer(f'Command "{msg.text}" doesnt exist')