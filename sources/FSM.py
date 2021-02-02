from aiogram.dispatcher.filters.state import State, StatesGroup


class set_value(StatesGroup):
    value = State()
