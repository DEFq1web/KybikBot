from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from external import async_log_function_call

from aiogram import Router

r = Router()

@r.message(Command("start"))
@async_log_function_call
async def start(message: Message) -> None:
    await message.answer(
        f"Вітаю, {message.from_user.full_name}!\n"
        "Я перший бот Python розробника @sxyDef\n"
        "Этот бот предназначен для управления списком фильмов. С его помощью ты можешь\n"
        " Просматривать список фильмов\n"
        "➕ Добавлять фильмы\n"
        "➖ Удалять фильмы\n"
        "🧹 Очищать весь список\n"
        "🔍 Искать, фильтровать и редактировать фильмы\n"
        )
    