from typing import ChainMap
from aiogram.types import InlineKeyboardButton as IB
from aiogram.types import InlineKeyboardMarkup as IM
from aiogram.types import KeyboardButton as RB
from aiogram.types import ReplyKeyboardMarkup as RM
from aiogram.types import ReplyKeyboardRemove


class group:
    owner_not_found = IM().add(
        IB("🔁 Повторить поиск", callback_data="restart_owner_find")
    )


class private:
    invite = IM().add(
        IB("🆕 Пригласить бота", url="t.me/TGen_bot?startgroup=True")
    )

    class settings:
        settings = {
            "s_openGen": "🔤 Общедоступная база",
            "s_percent": "💬 Шанс генерации сообщения",
            "s_ping":    "💬 Упоминания",
            "s_memGen":  "💬 Генерирация мемов"
        }
        settings = IM(row_width=1).add(
            IB("🔤 Общедоступная база", callback_data="s_openGen"),
            IB("💬 Шанс генерации сообщения", callback_data="s_percent"),
            IB("💬 Упоминания", callback_data="s_ping"),
            IB("💬 Генерирация мемов", callback_data="s_memGen")
        )
