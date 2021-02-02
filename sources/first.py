from aiogram import types
from bot import dp
from sources import stickers, text


@dp.errors_handler()
async def errors(update: types.Update, error: Exception):
    msg = None
    if update.message:
        msg = update.message
    elif update.callback_query:
        msg = update.callback_query.message
    errorText = error.args[0]
    ignore = ["Message is not modified: specified new message content and reply markup are exactly the same as a current content and reply markup of the message",
              ""
              ]

    if errorText in ignore:
        return True
    elif errorText in text.error.errors:
        # await msg.answer_sticker(stickers.boom)
        await msg.answer(errorText)
        return True
    else:
        return None
