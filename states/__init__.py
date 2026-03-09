from aiogram.fsm.state import State, StatesGroup

class ReportStates(StatesGroup):
    caption = State()
    price = State()

class AdminStates(StatesGroup):
    add_money = State()
