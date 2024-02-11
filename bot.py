import asyncio
import logging

from aiogram import Dispatcher, Bot

from config_data.config import Config, load_config
from keyboards.main_menu import set_main_menu


# Logger init
logger = logging.getLogger(__name__)


async def main():
    # Logging configuration
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    logger.info('Starting bot')

    # Loading config
    config: Config = load_config()

    # Bot and dispatcher init
    bot = Bot(token=config.tg_bot.token,
              parse_mode='HTML')
    dp = Dispatcher()

    # Setting bots main menu
    await set_main_menu(bot)

    # including other routers
    # dp.include_router(user_handlers.router)
    # dp.include_router(admin_handlers.router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())