from typing import *

from aiogram import types
from aiogram.dispatcher import FSMContext
from bot import bot, dp
from sources import text, buttons
from sources.private import private


def find_member(msg: types.Message) -> bool:
    members = msg.new_chat_members
    result = False
    for u in members:
        if u.id == msg.from_user.id:
            result = True
            break
    else:
        result = False


@dp.callback_query_handler(lambda msg: msg.data == "restart_owner_find" and msg.message.chat.type in ["supergroup", "group"])
@dp.message_handler(lambda msg: msg.chat.type in ["supergroup", "group"], content_types=[types.ContentType.NEW_CHAT_MEMBERS])
async def join(msg: Union[types.Message, types.CallbackQuery], state: FSMContext):
    if type(msg) == types.CallbackQuery:
        msg = msg.message
    try:
        await msg.delete()
    except:
        pass
    find = find_member(msg)

    admins = await msg.chat.get_administrators()
    for admin in admins:
        if admin.is_chat_creator():
            id = admin.user.id
            try:
                await bot.send_message(id, text.private.invited)
            except:
                await msg.answer(text.group.owner_not_start.format(admin.user.mention), reply_markup=buttons.group.owner_not_found)
                break
            await msg.answer(text.group.start)
            await private.settings(msg, msg.chat.id)
            break
    else:
        await msg.answer(text.group.owner_not_found, reply_markup=buttons.group.owner_not_found)
