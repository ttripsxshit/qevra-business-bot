from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from keyboards.inline import (
    calculator_keyboard,
    bot_type_keyboard,
    result_keyboard,
)

router = Router()


@router.message(F.text == "💸 Калькулятор")
async def calculator_start(message: Message):
    await message.answer(
        "💸 Калькулятор стоимости\n\n"
        "Что тебя интересует?",
        reply_markup=calculator_keyboard,
    )


@router.callback_query(F.data == "start_calculator")
async def calculator_start_callback(callback: CallbackQuery):
    await callback.message.answer(
        "💸 Калькулятор стоимости\n\n"
        "Что тебя интересует?",
        reply_markup=calculator_keyboard,
    )
    await callback.answer()


@router.callback_query(F.data == "calc_bot")
async def calc_bot(callback: CallbackQuery):
    await callback.message.answer(
        "🤖 Какой бот нужен?",
        reply_markup=bot_type_keyboard,
    )
    await callback.answer()


@router.callback_query(F.data == "bot_simple")
async def bot_simple(callback: CallbackQuery):
    await callback.message.answer(
        "💰 Примерная стоимость:\n\n"
        "от 3 500 ₽ до 7 000 ₽\n\n"
        "Подойдет для:\n"
        "• бот-визитки\n"
        "• меню услуг\n"
        "• записи\n"
        "• контактов\n"
        "• простой навигации\n\n"
        "Хороший вариант, если нужен аккуратный бот без сложной логики.",
        reply_markup=result_keyboard,
    )
    await callback.answer()


@router.callback_query(F.data == "bot_medium")
async def bot_medium(callback: CallbackQuery):
    await callback.message.answer(
        "💰 Примерная стоимость:\n\n"
        "от 7 000 ₽ до 15 000 ₽\n\n"
        "Подойдет для:\n"
        "• заявок\n"
        "• нескольких разделов\n"
        "• FAQ\n"
        "• кейсов\n"
        "• прайса\n"
        "• удобной навигации\n\n"
        "Это уже не просто визитка, а нормальная мини-воронка внутри Telegram.",
        reply_markup=result_keyboard,
    )
    await callback.answer()


@router.callback_query(F.data == "bot_ai")
async def bot_ai(callback: CallbackQuery):
    await callback.message.answer(
        "💰 Примерная стоимость:\n\n"
        "от 20 000 ₽ до 35 000 ₽\n\n"
        "Подойдет для:\n"
        "• AI-функций\n"
        "• автоматизации\n"
        "• нестандартной логики\n"
        "• интеграций\n"
        "• умных ответов клиентам\n\n"
        "Тут уже собирается не просто бот, а помощник под конкретные задачи бизнеса.",
        reply_markup=result_keyboard,
    )
    await callback.answer()


@router.callback_query(F.data == "calc_cards")
async def calc_cards(callback: CallbackQuery):
    await callback.message.answer(
        "🛒 Карточки WB/Ozon\n\n"
        "Примерная стоимость:\n\n"
        "от 500 ₽ за карточку\n\n"
        "Цена зависит от:\n"
        "• количества слайдов\n"
        "• сложности дизайна\n"
        "• качества исходных фото\n"
        "• необходимости инфографики\n\n"
        "Если коротко: чем больше надо «вытащить» товар визуально, тем выше цена.",
        reply_markup=result_keyboard,
    )
    await callback.answer()


@router.callback_query(F.data == "calc_design")
async def calc_design(callback: CallbackQuery):
    await callback.message.answer(
        "🎨 Дизайн\n\n"
        "Примерная стоимость:\n\n"
        "от 1 000 ₽ до 7 000 ₽\n\n"
        "Подойдет для:\n"
        "• аватарок\n"
        "• баннеров\n"
        "• оформления Telegram\n"
        "• промо-картинок\n"
        "• простого визуала под проект\n\n"
        "Финальная цена зависит от объема и количества материалов.",
        reply_markup=result_keyboard,
    )
    await callback.answer()


@router.callback_query(F.data == "calc_auto")
async def calc_auto(callback: CallbackQuery):
    await callback.message.answer(
        "⚙️ Автоматизация бизнеса\n\n"
        "Примерная стоимость:\n\n"
        "от 7 000 ₽ до 30 000 ₽\n\n"
        "Подойдет для:\n"
        "• сбора заявок\n"
        "• уведомлений в Telegram\n"
        "• простых CRM-сценариев\n"
        "• автоворонок\n"
        "• связок под конкретную задачу\n\n"
        "Если ты каждый день делаешь одну и ту же ручную работу — скорее всего, её можно автоматизировать.",
        reply_markup=result_keyboard,
    )
    await callback.answer()