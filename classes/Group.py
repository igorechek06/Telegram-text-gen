import json
from typing import *

from aiogram.types import InlineKeyboardButton as IB
from aiogram.types import InlineKeyboardMarkup as IM
from aiogram.types import KeyboardButton as RB
from aiogram.types import ReplyKeyboardMarkup as RM
from aiogram.types import ReplyKeyboardRemove
from sources import buttons, text


def num_to_emj(num: int):
    e = "️⃣"
    return e.join(list(str(num))) + e


def nice_bool(bool: bool):
    return "✅" if bool else "⛔"


class Group:
    from . import Database as db

    def __init__(self, group_id: int, owner_id: int, settings: str, owner_auth: str, group_auth: str) -> None:
        self.Database = self.db.Database("./data/database.db")
        self.group_id = int(group_id)
        self.owner_id = int(owner_id)
        self.settings: Mapping[str, Union[bool, int]] = \
            dict(json.loads(settings))
        self.owner_auth = str(owner_auth)
        self.group_auth = str(group_auth)

    async def set_settings(self, settings: Union[str, dict]):
        settings_str = ""
        if type(settings) == dict:
            self.settings = settings
            settings_str = json.dumps(self.settings)
        elif type(settings) == str:
            settings_str = settings
            self.settings == dict(json.loads(settings))

        self.Database.set_settings(
            self.group_id, settings_str
        )

    @property
    def settings_text(self):
        txt = text.private.settings.settings
        reply_markup = buttons.private.settings.settings
        format = [self.group_auth]

        for key in self.settings:
            value = self.settings[key]
            add_txt = ""
            if type(value) == int:
                add_txt = num_to_emj(value)
            elif type(value) == bool:
                add_txt = nice_bool(value)
            format.append(add_txt)

        return txt.format(*format), reply_markup
