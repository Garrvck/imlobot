from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

check_button = InlineKeyboardButton(text="✅ Obuna bo\'ldim", callback_data="check_subs")

channels_button = InlineKeyboardMarkup(row_width=1)
channels_button.insert(InlineKeyboardButton(text=f"1-kanal", url="https://t.me/+RPttJumoKzeVF08j"))
# channels_button.insert(InlineKeyboardButton(text=f"2-kanal", url="https://t.me/+hmvkN9gIqoJjMjhi"))
# channels_button.insert(InlineKeyboardButton(text=f"3-kanal", url="https://t.me/+RPttJumoKzeVF08j"))
channels_button.insert(check_button)

accept = InlineKeyboardMarkup(row_width=1)
accept.insert(InlineKeyboardButton(text='Roziman', callback_data='accept'))