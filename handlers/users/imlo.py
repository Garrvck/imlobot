from aiogram import types, Bot, Dispatcher, executor
from loader import dp
from utils.misc.checkWord import checkWords
from data.transliterate import to_latin, to_cyrillic

# @dp.message_handler()
# async def chekword(message: types.Message):
#     word = message.text
#
#     result = checkWords(word)
#     if result['available']:
#         response = f"✅ {word.capitalize()}"
#     else:
#         response = f"❌ {word.capitalize()}\n"
#         for text in result['matches']:
#             response += f"✅ {text.capitalize()}\n"
#     await message.answer(response)




@dp.message_handler()
async def chekword(message: types.Message):
    word = message.text
    lotin = False
    #alifboni tekshirish
    if word.isascii():
        lotin = True
        word = to_cyrillic(word)

    result = checkWords(word)
    if result['available']:
        if lotin:
            response = f"✅ {to_latin(word.capitalize())}"
        else:
            response = f"✅ {word.capitalize()}"

    else:
        if lotin:
            response = f"❌ {to_latin(word.capitalize())}\n"
        else:
            response = f"❌ {word.capitalize()}\n"
        for text in result['matches']:
            if lotin:
                response += f"✅ {to_latin(text.capitalize())}\n"
            else:
                response += f"✅ {text.capitalize()}\n"
    await message.answer(response)

