import asyncio
from re import search

from aiogram import Router, Bot
from aiogram.types import Message, CallbackQuery ,InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.fsm.context import FSMContext

router = Router()


@router.message()
async def all_message(message: Message, bot: Bot):
	await asyncio.sleep(0.5)
	if message.entities is not None:
		url_data = message.entities[0].url
		if search('telegra.ph', url_data) is not None:
			text: str = message.text
			await message.delete()

			buttons = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Основной канал', url="https://t.me/zakupki_team")]])
			await bot.send_message(message.chat.id, f"<a href='{url_data}'>{text}</a>", reply_markup=buttons, parse_mode="HTML")
