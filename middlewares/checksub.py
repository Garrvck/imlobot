from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

from data.config import CHANNELS
from utils.misc import subscription
from keyboards.inline.subscription import channels_button



class BigBrother(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        if update.message:
            user = update.message.from_user.id
            if update.message.text in ['/help']:
                return
        elif update.callback_query:
            user = update.callback_query.from_user.id
            if update.callback_query.data == "check_subs":
                return
        else:
            return

        result = "Botdan foydalanish uchun quyidagi kanalga a'zo bo'ling.\n"
        final_status = 1
        for channel in CHANNELS:
            status = await subscription.check(user_id=user, channel=channel)
            if status == 'left':
                final_status = 0
        if not final_status:
            await update.message.answer(text=result, reply_markup=channels_button)
            raise CancelHandler()
