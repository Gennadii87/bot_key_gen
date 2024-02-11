import asyncio
import logging
import sys
from config import BOT_TOKEN
import re
from aiogram import Bot, Dispatcher, types, Router
from aiogram.enums import ParseMode
from aiogram.filters import Command
from keygen.keygen import KeyGen
from app_bot.config import len_check

TOKEN = BOT_TOKEN

dp = Dispatcher()
router = Router()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):

    kb = [
        [
            types.KeyboardButton(text=f'оптимальная длинна {len_check}'),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=False,
        input_field_placeholder="Количество символов пароля"
    )
    await message.answer("Сгенерировать пароль?", reply_markup=keyboard)


@dp.message()
async def with_puree(message: types.Message):
    length = re.findall(r'\d+', message.text)
    if length:
        key_gen = KeyGen(length[0])
        await message.reply(f'{key_gen}')
    else:
        await message.reply("Ошибка: Не могу найти число в вашем сообщении")


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
