import re
from typing import *

from aiogram import types
from aiogram.dispatcher import FSMContext
from bot import bot, dp
from classes import Group
from classes.Errors import *
from objects import Database
from sources import buttons, text, FSM
from sources.private import private
from objects import MessageData


@dp.callback_query_handler(lambda msg: re.match(text.system.patterns.select, msg.data))
async def select(callback: types.CallbackQuery, state: FSMContext):
    call_data = callback.data
    match = re.match(text.system.patterns.select, call_data)
    msg = callback.message

    id = match.group("id")

    await msg.delete()
    await private.settings(callback, group_id=id)


@dp.callback_query_handler(lambda msg: msg.data[2:] in text.private.settings.settings_default)
async def settings(callback: types.CallbackQuery, state: FSMContext):
    call_data = callback.data[2:]
    msg = callback.message

    data = await MessageData.get_data(msg.message_id)
    group = data["group"]  # type:Group
    settings = group.settings
    if type(settings[call_data]) == bool:
        settings[call_data] = not settings[call_data]
        await group.set_settings(settings)
        txt, reply_markup = group.settings_text
        await msg.edit_text(txt, reply_markup=reply_markup)
    else:
        await set_value(msg, state, group, call_data, type(settings[call_data]))


async def set_value(msg: types.Message, state: FSMContext, group: Group, value: str, type: Any):
    await msg.edit_text(text.private.settings.set_value[type])
    await FSM.set_value.value.set()

    async with state.proxy() as data:
        data["group_id"] = group.group_id
        data["type"] = type
        data["msg"] = msg
        data["value"] = value


@dp.edited_message_handler(content_types=[types.ContentType.TEXT], state=FSM.set_value.value)
@dp.message_handler(content_types=[types.ContentType.TEXT], state=FSM.set_value.value)
async def get_value(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        group = Database.get_group(data["group_id"])  # type:Group
        type = data["type"]
        bot_msg = data["msg"]  # type:types.Message
        value = data["value"]  # type:str

    if not re.match(text.system.patterns.set_value[type], msg.text):
        raise ArgumentError()

    if type == int and int(msg.text) > 75:
        raise ArgumentError()

    await msg.delete()
    settings = group.settings
    settings[value] = type(msg.text)
    await group.set_settings(settings)
    await state.finish()
    txt, reply_markup = group.settings_text
    await bot_msg.edit_text(txt, reply_markup=reply_markup)
