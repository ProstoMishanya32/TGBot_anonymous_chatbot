import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from colorama import init, Fore, Style

from handlers.user import start_user, settings, interests, anonumous_chat
from utils.configs_logic import config_manager
from utils.configs_logic.config_reader import config
from utils.miscellaneous.logging_logic import logger

from utils.services import db

init(autoreset=True)  # Иницилизация модуля colorama


async def main():
    db.start_sqlite()  # Подключение БД

    bot = Bot(token=config.token_bot.get_secret_value(), parse_mode=ParseMode.HTML)  # Сам обьект бота
    dp = Dispatcher()  # Диспетчер


    logger.info("База данных подключена")
    print(f"{Fore.GREEN}Добро пожаловать в мир бота, разработанного {Fore.MAGENTA}@michaailcoding{Fore.GREEN}!")
    print(f"Создан специально для {Fore.YELLOW}realsadyk{Fore.GREEN}. Посетите мой профиль на Kwork: {Fore.BLUE}{Style.BRIGHT}https://kwork.ru/user/michailcoding32{Style.NORMAL}")

    # Регистрация роутеров пользовательских Handlers
    dp.include_routers(start_user.router, settings.router, interests.router, anonumous_chat.router)

    main_admin = config_manager.get_value("main_admin")

    await bot.send_message(chat_id=main_admin,
                           text="➖➖➖ Бот зашел в сеть 🌐 ➖➖➖\n"
                                "<b>В случае возникновения каких-либо неполадок или вопросов, просьба обращаться к @michailcoding, вашему верному техническому соратнику.</b>")

    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
