from aiogram import types

async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Запустить бота'),
        types.BotCommand('show', 'Показать наличие и описание'),
        types.BotCommand('help', 'Помощь')
    ])