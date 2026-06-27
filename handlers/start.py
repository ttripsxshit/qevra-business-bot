from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from keyboards.reply import main_menu

router = Router()


WELCOME_TEXT = (
    "Йоу 👋\n\n"
    "Это ttripsxshit bot.\n\n"
    "Тут можно:\n"
    "— посмотреть услуги\n"
    "— прикинуть стоимость\n"
    "— глянуть кейсы\n"
    "— оставить заявку\n"
    "— не умереть от духоты\n\n"
    "Выбирай, что нужно 👇"
)


@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(WELCOME_TEXT, reply_markup=main_menu)


@router.callback_query(F.data == "back_main")
async def back_main(callback: CallbackQuery):
    await callback.message.answer(WELCOME_TEXT, reply_markup=main_menu)
    await callback.answer()


@router.message(F.text == "📲 Связаться")
async def contacts(message: Message):
    await message.answer(
        "Связь со мной — прямо тут в Telegram.\n\n"
        "Лучше нажми «📝 Оставить заявку», чтобы я сразу понял задачу.",
        reply_markup=main_menu,
    )