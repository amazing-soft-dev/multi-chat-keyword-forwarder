import asyncio
from aiogram import Router
from aiogram.enums import ChatType
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from utils.logger import get_logger
from states.all_states import JoinStates
from utils.join_groups import join_groups
from utils.special_func import is_user_allowed, clean_links

join_router = Router()
logger = get_logger(__name__)


@join_router.message(Command("join"))
async def save_filters(message: Message, state: FSMContext):
        """Обработчик команды /join"""
        if message.chat.type != ChatType.PRIVATE:
            return

        if not is_user_allowed(message.from_user.id):
            await message.answer("⛔ Доступ запрещён.")
            return

        text = (
                "🔍 Введите ссылки на группы в которые необходимо вступить (Ввод через проблел и в любом формате, но лучше как channel2)\n\n"
                "Пример ввода: https://t.me/channel1 @channel2 channel2"
        )

        await state.set_state(JoinStates.join)
        await message.answer(text)
        logger.info(f"Пользователь {message.from_user.id} запросил /join")


@join_router.message(JoinStates.join)
async def save_filters(message: Message, state: FSMContext):
        """Обработчик команды /join"""
        if message.chat.type != ChatType.PRIVATE:
            return

        if not is_user_allowed(message.from_user.id):
            await message.answer("⛔ Доступ запрещён.")
            return

        group_list = clean_links(message.text.lower().split())


        text = (
                f"Отправляются запросы на вступление...\n\nЧаты: {group_list}"
        )
        await message.answer(text)
        response = await asyncio.to_thread(join_groups, group_list)

        await state.clear()
        await message.answer(f"Успешно отпралвено {response} запросов на вступление")
        logger.info(f"Пользователь {message.from_user.id} ввел группы")