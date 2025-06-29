import logging
from bot import dp, bot, start_monitoring
import asyncio
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные окружения

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

async def main():
    await start_monitoring()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())