from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message()
async def smart_answers(message: Message):
    text = message.text.lower()

    if any(word in text for word in ["цена", "стоимость", "сколько стоит", "прайс"]):
        await message.answer(
            "💰 Стоимость зависит от проекта.\n\n"
            "Примерно:\n"
            "• Простые Telegram-боты — от 3 500 ₽\n"
            "• Средние проекты — от 7 000 ₽\n"
            "• AI и сложная автоматизация — до 35 000 ₽.\n\n"
            "Если расскажешь задачу, я смогу назвать более точную стоимость."
        )
        return

    if any(word in text for word in ["срок", "сроки", "долго", "время"]):
        await message.answer(
            "⏳ Обычно разработка занимает от 2 до 14 дней.\n\n"
            "Если проект большой — сроки обсуждаются отдельно."
        )
        return

    if any(word in text for word in ["бот", "телеграм", "telegram"]):
        await message.answer(
            "🤖 Делаю Telegram-ботов любой сложности.\n\n"
            "От простых ботов-визиток до AI-ботов и автоматизации бизнеса."
        )
        return

    if any(word in text for word in ["автоматизация", "crm", "заявки"]):
        await message.answer(
            "⚙️ Автоматизирую рутинные задачи.\n\n"
            "Например:\n"
            "• сбор заявок\n"
            "• уведомления\n"
            "• Telegram-боты\n"
            "• интеграции\n"
            "• простые CRM."
        )
        return

    if any(word in text for word in ["дизайн", "баннер", "логотип"]):
        await message.answer(
            "🎨 Также занимаюсь дизайном.\n\n"
            "• баннеры\n"
            "• оформление Telegram\n"
            "• карточки WB/Ozon\n"
            "• промо-материалы."
        )
        return

    if any(word in text for word in ["wb", "ozon", "карточки"]):
        await message.answer(
            "🛒 Делаю карточки товаров для WB и Ozon.\n\n"
            "Стоимость начинается от 500 ₽ за карточку."
        )
        return

    await message.answer(
        "🤔 Пока не совсем понял вопрос.\n\n"
        "Попробуй написать иначе или нажми «📩 Обсудить проект», и мы разберём задачу вместе."
    )