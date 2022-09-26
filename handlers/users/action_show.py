import logging

from aiogram.types import CallbackQuery
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp


from keyboards.reply.ch_type_kb import ch_type_kb
from keyboards.reply.show_again_kb import show_again_kb
from states import show_state
from data import config


@dp.callback_query_handler(text='show')
async def show_ch_type_kb(call: CallbackQuery):
    await dp.bot.answer_callback_query(call.id)
    await call.message.answer('Выберите что показать', reply_markup=ch_type_kb)
    await show_state.typeOf.set()

@dp.message_handler(text='Выбрать другое')
async def show_ch_type_kb(msg: types.Message):
    await msg.answer('Выберите что показать', reply_markup=ch_type_kb)
    await show_state.typeOf.set()

@dp.message_handler(text='В начало')
async def go_to_start(msg: types.Message):
    await dp.bot.send_message(msg.from_user.id,'Введите /start')

@dp.message_handler(state=show_state.typeOf)
async def step1(msg: types.Message, state:FSMContext):
        ent_type = msg.text
        await state.update_data(typeOf=ent_type)
        await msg.answer(f'Вы выбрали {ent_type}\n'
                     f'{config.garlands.get(ent_type).to_string(index=False)}\n'
                     f'Что делаем дальше?', reply_markup=show_again_kb)
        await state.finish()

