from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from keyboards.inline import services_keyboard, service_action_keyboard

router = Router()


SERVICES_TEXT = (
    "🧩 Услуги\n\n"
    "Что делаем?\n\n"
    "🤖 Telegram-боты — от простых визиток до AI-ботов\n"
    "🛒 Карточки WB/Ozon — чтобы товар не выглядел как фото с табуретки\n"
    "⚙️ Автоматизация — убираем ручную возню\n"
    "🎨 Дизайн — визуал для проектов\n\n"
    "Выбирай раздел 👇"
)


@router.message(F.text == "🧩 Услуги")
async def services_menu(message: Message):
    await message.answer(SERVICES_TEXT, reply_markup=services_keyboard)


@router.callback_query(F.data == "back_services")
async def back_services(callback: CallbackQuery):
    await callback.message.answer(SERVICES_TEXT, reply_markup=services_keyboard)
    await callback.answer()


@router.callback_query(F.data == "service_bots")
async def service_bots(callback: CallbackQuery):
    await callback.message.answer(
        "🤖 Telegram-боты\n\n"
        "Делаю ботов под задачи бизнеса:\n\n"
        "— бот-визитка\n"
        "— запись клиентов\n"
        "— меню услуг\n"
        "— заявки в админку\n"
        "— FAQ\n"
        "— калькуляторы\n"
        "— AI-функции\n"
        "— запуск на VPS\n\n"
        "Цена: от 3 500 ₽ до 35 000 ₽.\n\n"
        "Если коротко: можно сделать простую визитку, а можно собрать мини-систему, "
        "которая реально экономит время.",
        reply_markup=service_action_keyboard,
    )
    await callback.answer()


@router.callback_query(F.data == "service_cards")
async def service_cards(callback: CallbackQuery):
    await callback.message.answer(
        "🛒 Карточки WB/Ozon\n\n"
        "Делаю карточки для маркетплейсов, чтобы товар выглядел не как "
        "«ну я сфоткал, вроде норм».\n\n"
        "Что входит:\n"
        "— инфографика\n"
        "— преимущества товара\n"
        "— единый стиль\n"
        "— чистый визуал\n"
        "— подготовка под WB/Ozon\n\n"
        "Цена: от 500 ₽ за карточку.",
        reply_markup=service_action_keyboard,
    )
    await callback.answer()


@router.callback_query(F.data == "service_auto")
async def service_auto(callback: CallbackQuery):
    await callback.message.answer(
        "⚙️ Автоматизация бизнеса\n\n"
        "Помогаю убрать ручную возню:\n\n"
        "— сбор заявок\n"
        "— уведомления в Telegram\n"
        "— простые CRM-сценарии\n"
        "— автоворонки\n"
        "— боты-помощники\n"
        "— связки под конкретную задачу\n\n"
        "Если ты каждый день делаешь одно и то же руками — скорее всего, "
        "это можно автоматизировать.",
        reply_markup=service_action_keyboard,
    )
    await callback.answer()


@router.callback_query(F.data == "service_design")
async def service_design(callback: CallbackQuery):
    await callback.message.answer(
        "🎨 Дизайн\n\n"
        "Делаю визуал под проекты:\n\n"
        "— аватарки\n"
        "— баннеры\n"
        "— оформление Telegram\n"
        "— карточки\n"
        "— простые промо-картинки\n"
        "— визуал под стиль проекта\n\n"
        "Без «дорого-богато», но чтобы выглядело аккуратно и не стыдно.",
        reply_markup=service_action_keyboard,
    )
    await callback.answer()