from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage

storage = MemoryStorage()

class FiltersStates(StatesGroup):
    search = State()
    filter_words = State()
    ban_words = State()

class JoinStates(StatesGroup):
    join = State()
