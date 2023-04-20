from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS, CHANNELS
import sqlite3
from utils.misc import subscription
from loader import dp, bot, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id, fullname=name)
    except sqlite3.IntegrityError as err:
        pass
    await message.answer(f"Salom, {message.from_user.full_name}!")
    count = db.count_users()[0]
    msg = f"➕ {message.from_user.full_name}.\nJami - <b>{count}</b>"
    await bot.send_message(chat_id=ADMINS[0], text=msg)

@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery):
    final_status = True
    for channel in CHANNELS:
        status = await subscription.check(user_id=call.from_user.id, channel=channel)
        if status == 'left':
            final_status = False
    if final_status:
        name = call.from_user.full_name
        try:
            db.add_user(id=call.from_user.id, fullname=name)
        except sqlite3.IntegrityError as err:
            pass
        count = db.count_users()[0]
        msg = f"➕ {call.from_user.full_name}.\nJami - <b>{count}</b>"
        await bot.send_message(chat_id=ADMINS[0], text=msg)
        await call.message.delete()
        await call.message.answer(text=f"Salom, {call.from_user.full_name}!")
    else:
        await call.answer(text="⚠️ Kanallarga obuna bo'ling", show_alert=True)
