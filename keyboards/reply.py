from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🧩 Услуги"),
            KeyboardButton(text="💸 Калькулятор"),
        ],
        [
            KeyboardButton(text="📂 Кейсы"),
            KeyboardButton(text="📩 Обсудить проект"),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выбери раздел или напиши вопрос 👇",
)


cancel_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="❌ Отменить заявку"),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="Заполнение заявки",
)