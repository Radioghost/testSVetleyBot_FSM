from aiogram.dispatcher.filters.state import StatesGroup, State

class add_state(StatesGroup):
    typeOf = State()
    len = State()
    date = State()
    descr = State()