from aiogram.filters import Command
from aiogram.types.bot_command import BotCommand

START_COMMAND = Command('start')
FILMS_COMMAND = Command('films')
FILM_CREATE_COMMAND = Command("create_film")
FILM_FILTER_COMMAND = Command("filter_movie")
FILM_SEARCH_COMMAND = Command("search_movie")


BOT_COMMANDS = [
    BotCommand(command="start", description="Почати розмову"),
   BotCommand(command="films", description="Перегляд списку фільмів"),
   BotCommand(command="create_film", description="Додати новий фільм"),
   BotCommand(command="search_movie", description="Знайти фільм"),
   BotCommand(command="filter_movie", description="Фільтрувати фільми"),
]