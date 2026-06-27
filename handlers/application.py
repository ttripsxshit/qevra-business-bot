from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from config.config import ADMIN_ID
from keyboards.reply import main_menu, cancel_keyboard
from states.application_state import ApplicationState

router = Router()

CANCEL_TEXT = "❌ Отменить заявку"


@router.message(F.text == "📩 Обсудить проект")
async def start_application(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(ApplicationState.name)

    await message.answer(
        "👋 Отлично!\n\n"
        "Я задам несколько вопросов, чтобы понять задачу и оценить проект.",
        reply_markup=cancel_keyboard,
    )

    await message.answer("Как тебя зовут?")


@router.message(F.text == CANCEL_TEXT)
async def cancel_application(message: Message, state: FSMContext):
    await state.clear()

    await message.answer(
        "✅ Заявка отменена.",
        reply_markup=main_menu,
    )


@router.message(ApplicationState.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)

    await state.set_state(ApplicationState.niche)

    await message.answer(
        "💼 Чем ты занимаешься?\n\n"
        "Например:\n"
        "• Магазин\n"
        "• Салон красоты\n"
        "• Онлайн-школа\n"
        "• Автосервис"
    )


@router.message(ApplicationState.niche)
async def get_niche(message: Message, state: FSMContext):
    await state.update_data(niche=message.text)

    await state.set_state(ApplicationState.project)

    await message.answer(
        "📄 Опиши кратко, какой проект нужен."
    )


@router.message(ApplicationState.project)
async def get_project(message: Message, state: FSMContext):
    await state.update_data(project=message.text)

    await state.set_state(ApplicationState.example)

    await message.answer(
        "📎 Есть примеры?\n\n"
        "Если нет — просто напиши «нет»."
    )


@router.message(ApplicationState.example)
async def get_example(message: Message, state: FSMContext):
    await state.update_data(example=message.text)

    await state.set_state(ApplicationState.deadline)

    await message.answer(
        "⏳ Когда нужен проект?"
    )


@router.message(ApplicationState.deadline)
async def get_deadline(message: Message, state: FSMContext):
    await state.update_data(deadline=message.text)

    await state.set_state(ApplicationState.contact)

    username = (
        f"@{message.from_user.username}"
        if message.from_user.username
        else ""
    )

    if username:
        await message.answer(
            "📲 Как с тобой связаться?\n\n"
            f"Можно оставить этот Telegram:\n{username}\n\n"
            "Или отправить другой контакт."
        )
    else:
        await message.answer(
            "📲 Оставь Telegram или другой способ связи."
        )


@router.message(ApplicationState.contact)
async def finish_application(message: Message, state: FSMContext):
    data = await state.get_data()

    contact = message.text

    text = (
        "🔥 НОВАЯ ЗАЯВКА\n\n"
        f"👤 Имя:\n{data['name']}\n\n"
        f"💼 Ниша:\n{data['niche']}\n\n"
        f"📄 Проект:\n{data['project']}\n\n"
        f"📎 Примеры:\n{data['example']}\n\n"
        f"⏳ Дедлайн:\n{data['deadline']}\n\n"
        f"📲 Контакт:\n{contact}\n\n"
        f"🆔 Telegram ID:\n{message.from_user.id}"
    )

    await message.bot.send_message(
        chat_id=ADMIN_ID,
        text=text,
    )

    await message.answer(
        "🚀 Спасибо!\n\n"
        "Заявка отправлена.\n"
        "Я свяжусь с тобой в ближайшее время.",
        reply_markup=main_menu,
    )

    await state.clear()
    