import asyncio
from aiogram import Bot, Dispatcher

from settings import settings
import commands

async def main():
	bot = Bot(settings.TOKEN)
	dp = Dispatcher()

	dp.include_router(commands.router)

	print("BOT WORKS")
	await bot.delete_webhook(drop_pending_updates=True)
	await dp.start_polling(bot)


if __name__ == '__main__':
	try:
		asyncio.run(main())
	except KeyboardInterrupt:
		print("\n@GoodBye :)")
