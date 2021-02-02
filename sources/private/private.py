from typing import *

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton as IB
from aiogram.types import InlineKeyboardMarkup as IM
from bot import bot, dp
from classes import Group
from classes.Errors import *
from objects import Database, MessageData
from sources import buttons, text


@dp.message_handler(lambda msg: msg.chat.type == "private", commands=["start"])
async def start(msg: types.Message):
    await msg.answer(text.private.start, reply_markup=buttons.private.invite)


@dp.message_handler(lambda msg: msg.chat.type == "private", commands=["settings"])
async def group_select(msg: types.Message):
    groups = Database.get_groups(msg.from_user.id)  # type:List[Group]
    if groups is None:
        raise NotGroupOwned()

    reply_markup = IM()

    for group in groups:
        reply_markup.add(
            IB(group.group_auth, callback_data=f"sel_{group.group_id}")
        )
    await msg.answer(text.private.settings.select, reply_markup=reply_markup)


async def settings(msg: types.Message, group_id: int):
    group = Database.get_group(group_id)  # type:Group
    if group is None:
        settings = text.private.settings.settings_default
        Database.add_group_settings(msg, settings)
        group = Database.get_group(group_id)  # type:Group

    txt, reply_markup = group.settings_text
    bot_msg = await bot.send_message(msg.from_user.id, txt, reply_markup=reply_markup)
    await MessageData.add_data(bot_msg.message_id, {"group": group})
