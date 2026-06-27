from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


services_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🤖 Telegram-боты", callback_data="service_bots")],
        [InlineKeyboardButton(text="🛒 Карточки WB/Ozon", callback_data="service_cards")],
        [InlineKeyboardButton(text="⚙️ Автоматизация бизнеса", callback_data="service_auto")],
        [InlineKeyboardButton(text="🎨 Дизайн", callback_data="service_design")],
        [InlineKeyboardButton(text="⬅️ В меню", callback_data="back_main")],
    ]
)


service_action_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📝 Оставить заявку", callback_data="start_application")],
        [InlineKeyboardButton(text="💸 Рассчитать цену", callback_data="start_calculator")],
        [InlineKeyboardButton(text="⬅️ Назад к услугам", callback_data="back_services")],
    ]
)


cases_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="💅 Мастер ногтевого сервиса", callback_data="case_nails")],
        [InlineKeyboardButton(text="✨ Косметолог-эстетист", callback_data="case_cosmetologist")],
        [InlineKeyboardButton(text="⬅️ В меню", callback_data="back_main")],
    ]
)


case_action_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📝 Хочу так же", callback_data="start_application")],
        [InlineKeyboardButton(text="⬅️ Назад к кейсам", callback_data="back_cases")],
    ]
)


calculator_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🤖 Telegram-бот", callback_data="calc_bot")],
        [InlineKeyboardButton(text="🛒 Карточки WB/Ozon", callback_data="calc_cards")],
        [InlineKeyboardButton(text="🎨 Дизайн", callback_data="calc_design")],
        [InlineKeyboardButton(text="⚙️ Автоматизация", callback_data="calc_auto")],
        [InlineKeyboardButton(text="⬅️ В меню", callback_data="back_main")],
    ]
)


bot_type_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Простой бот", callback_data="bot_simple")],
        [InlineKeyboardButton(text="Средний проект", callback_data="bot_medium")],
        [InlineKeyboardButton(text="AI / сложный проект", callback_data="bot_ai")],
        [InlineKeyboardButton(text="⬅️ Назад к калькулятору", callback_data="start_calculator")],
    ]
)


result_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📝 Оставить заявку", callback_data="start_application")],
        [InlineKeyboardButton(text="💸 Рассчитать ещё", callback_data="start_calculator")],
        [InlineKeyboardButton(text="⬅️ В меню", callback_data="back_main")],
    ]
)


back_to_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ В меню", callback_data="back_main")]
    ]
)