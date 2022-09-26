#import modules
import pandas as pd
from aiogram.types import CallbackQuery
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from data.config import garlands
from data import gars

#import files
from data import config
from keyboards.reply.ch_type_kb import ch_type_kb
from states import add_state
from keyboards.reply.yn_kb import yn_kb
from data.config import setDateAndDescrToLen


@dp.callback_query_handler(text='add')
async def show_ch_type_kb(call: CallbackQuery):
    await dp.bot.answer_callback_query(call.id)
    await call.message.answer('Куда добавлять будем?', reply_markup=ch_type_kb)
    await add_state.typeOf.set()

@dp.message_handler(text='Нет')
async def show_ch_type_kb(msg: types.Message):
    await msg.answer('Куда добавлять будем?', reply_markup=ch_type_kb)
    await add_state.typeOf.set()

@dp.message_handler(state=add_state.typeOf)
async def step1(msg: types.Message, state: FSMContext):
    ent_type = msg.text
    if ent_type not in config.garlands:
        await state.finish()
        await dp.bot.send_message(msg.from_user.id, 'Start from /start')

    await state.update_data(typeOf=ent_type)
    await add_state.len.set()
    await msg.answer(f'Вы выбрали {ent_type}\n'
                     f'Вот описание \n'
                     f'{config.garlands.get(ent_type).to_string(index=False)}\n'
                     f' Какая длинна вас интересует')

@dp.message_handler(state=add_state.len)
async def step2(msg: types.Message, state:FSMContext):
    data = await state.get_data()
    ent_type = data.get('typeOf')
    ent_len = msg.text
    nlen = int(ent_len)
    await state.update_data(len=ent_len)
    await add_state.date.set()
    df = config.garlands[f'{ent_type}'].copy()
    print(df)
    df['len'] = pd.to_numeric(df['len'], errors='coerce')
    idx = (df[df['len'] == nlen].index).to_list()
    print(df[['len','date','descr']])
    lists = list()
    for i in range(len(idx)):
        lists.append(df.iloc[idx[i]])


    await msg.answer(f'Вы выбрали: "{ent_type}", длинна: "{ent_len}"\n'
                     f'Вот описание: \n'
                     f'{lists}\n'
                     f'\n'
                     f'Введите дату, в формате "ГГГГ-ММ-ДД"')

@dp.message_handler(state=add_state.date)
async def step3(msg: types.Message, state: FSMContext, df = pd.DataFrame):
    data = await state.get_data()
    ent_type = data.get('typeOf')
    ent_len = data.get('len')
    ent_date = msg.text
    await state.update_data(date=ent_date)
    await add_state.descr.set()
    await msg.answer(f'Вы выбрали: "{ent_type}", длинна: "{ent_len}", дата: "{ent_date}"\n'
                     f'Введите описание')

@dp.message_handler(text='Да', state=add_state.descr)
async def show_result(msg: types.Message, state: FSMContext):
    await msg.answer(f' tryin to apply changes')
    data = await state.get_data()
    ent_type = data.get('typeOf')
    ent_len = int(data.get('len'))
    ent_date = data.get('date')
    ent_descr = data.get('descr')
    await setDateAndDescrToLen(ent_len, ent_date, ent_descr, config.garlands[f'{ent_type}'])
    await dp.bot.send_message(msg.from_user.id, f'{config.garlands.get(ent_type).to_string(index=False)}')
    await state.finish()

@dp.message_handler(state=add_state.descr)
async def step4(msg: types.Message, state: FSMContext):
    data = await state.get_data()
    ent_type = data.get('typeOf')
    ent_len = int(data.get('len'))
    ent_date = data.get('date')
    ent_descr = msg.text
    await state.update_data(descr=ent_descr)
    await msg.answer(f'Вы выбрали: "{ent_type}", длинна: "{ent_len}", дата: "{ent_date}", описание: "{ent_descr}\n"'
                     f'Все верно?', reply_markup=yn_kb)










