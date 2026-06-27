from aiogram.fsm.state import State, StatesGroup


class ApplicationState(StatesGroup):
    name = State()
    niche = State()
    project = State()
    example = State()
    deadline = State()
    contact = State()