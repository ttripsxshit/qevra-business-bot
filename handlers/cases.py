from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from keyboards.inline import cases_keyboard, case_action_keyboard

router = Router()


CASES_TEXT = (
    "📂 Кейсы\n\n"
    "Пока кейсов немного, но они живые, не из воздуха.\n\n"
    "Выбирай, что посмотреть 👇"
)


@router.message(F.text == "📂 Кейсы")
async def cases_menu(message: Message):
    await message.answer(CASES_TEXT, reply_markup=cases_keyboard)


@router.callback_query(F.data == "back_cases")
async def back_cases(callback: CallbackQuery):
    await callback.message.answer(CASES_TEXT, reply_markup=cases_keyboard)
    await callback.answer()


@router.callback_query(F.data == "case_nails")
async def case_nails(callback: CallbackQuery):
    await callback.message.answer(
        "💅 Кейс: Telegram-бот для мастера ногтевого сервиса\n\n"
        "Задача:\n"
        "Сделать бота для мастера ногтевого сервиса с услугами, прайсом, записью и понятной навигацией.\n\n"
        "Что было сделано:\n"
        "— главное меню\n"
        "— раздел с информацией о мастере\n"
        "— услуги\n"
        "— прайс\n"
        "— запись клиента\n"
        "— кнопки назад\n"
        "— запуск на VPS\n"
        "— автозапуск\n\n"
        "Результат:\n"
        "Клиент может посмотреть услуги и оставить заявку прямо в Telegram.",
        reply_markup=case_action_keyboard,
    )
    await callback.answer()


@router.callback_query(F.data == "case_cosmetologist")
async def case_cosmetologist(callback: CallbackQuery):
    await callback.message.answer(
        "✨ Кейс: Telegram-бот для косметолога-эстетиста\n\n"
        "Задача:\n"
        "Сделать бота для косметолога-эстетиста с презентацией услуг и сбором заявок.\n\n"
        "Что было сделано:\n"
        "— главное меню\n"
        "— разделы услуг\n"
        "— прайс\n"
        "— FAQ\n"
        "— контакты\n"
        "— сбор заявок\n"
        "— удобная навигация\n"
        "— запуск на VPS\n\n"
        "Результат:\n"
        "Бот работает как цифровая витрина специалиста и помогает принимать обращения клиентов.",
        reply_markup=case_action_keyboard,
    )
    await callback.answer()