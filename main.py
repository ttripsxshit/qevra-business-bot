import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config.config import BOT_TOKEN

from handlers import (
    start,
    services,
    cases,
    calculator,
    application,
    chat,
)


async def main():
    bot = Bot(token=BOT_TOKEN)

    dp = Dispatcher(
        storage=MemoryStorage()
    )

    
    dp.include_router(start.router)

  
    dp.include_router(services.router)
    dp.include_router(cases.router)
    dp.include_router(calculator.router)

    dp.include_router(application.router)
    dp.include_router(chat.router)

    print("ttripsxshit bot запущен")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())