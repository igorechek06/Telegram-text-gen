import json
from dataclasses import dataclass
from sqlite3 import connect
from typing import *

from aiogram import types
from sources import text


def get_mention(chat: types.Chat):
    if chat.username is None:
        return chat.full_name
    return chat.username


class Database:
    from . import Group as gp

    def __init__(self, path: str):
        self.connect = connect(path)
        self.cursor = self.connect.cursor()

    def run(self, sql: str, parameters: List = []) -> List[Any]:
        with self.connect:
            result = self.cursor.execute(sql, parameters)
            return result.fetchall()

    def get_text(self, group: str) -> List[str]:
        sql = f"SELECT text FROM {group}"
        result = self.run(sql)
        result = [i[0] for i in result]
        return result

    def get_groups(self, owner: str):
        sql = f"SELECT * FROM settings WHERE owner_id = '{owner}'"
        run = self.run(sql)
        result = []
        for r in run:
            result.append(self.gp.Group(*r))
        if not result:
            return None
        return result

    def get_group(self, group: str):
        sql = f"SELECT * FROM settings WHERE group_id = {group}"
        result = self.run(sql)
        if not result:
            return None
        return self.gp.Group(*result[0])

    def add_group_table(self, group: int):
        sql = f"CREATE TABLE {group} (text INTEGER);"
        self.run(sql)

    def add_group_settings(self, msg: types.Message, settings: dict = text.private.settings.settings_default):
        settings: str = json.dumps(settings)

        chat = msg.chat
        user = msg.from_user
        sql = f"INSERT INTO settings VALUES ({chat.id},{user.id},'{settings}','{user.mention}','{get_mention(chat)}')"
        self.run(sql)

    def set_settings(self, group_id: int, settings: str):
        sql = f"UPDATE settings SET settings = '{settings}' WHERE group_id = {group_id}"
        self.run(sql)


if __name__ == "__main__":
    db = Database("./data/database.db")
    print(db.get_group("123"))
