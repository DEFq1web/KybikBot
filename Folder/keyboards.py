from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData 

class FilmCallback(CallbackData, prefix="films", sep=","):
    id: int
    name: str

class PageCallback(CallbackData, prefix="page", sep=","):
    id: int

def films_keyboard_markup(films_list: list[dict], offset: int | None = None, skip: int | None = None, page=0):
    """
    Створює клавіатуру на основі отриманого списку фільмів
    """
    builder = InlineKeyboardBuilder()
    count = 6

    for index, film_data in enumerate(films_list[count * page : count * page + count]):
        # Важливо: вычисляем индекс фильма относительно всего списка
        real_index = count * page + index

        # Создаём объект CallbackData с real_index
        callback_data = FilmCallback(
            id=real_index,
            name=film_data["name"]
        )

        # Добавляем кнопку
        builder.button(
            text=f"{film_data['name']}",
            callback_data=callback_data.pack()
        )

    # Добавляем кнопки пагинации
    builder.button(
        text="📖 Минула сторінка",
        callback_data=PageCallback(id=page - 1).pack()
    )

    builder.button(
        text="📘 Наступна сторінка",
        callback_data=PageCallback(id=page + 1).pack()
    )

    builder.adjust(2, repeat=True)
    return builder.as_markup()