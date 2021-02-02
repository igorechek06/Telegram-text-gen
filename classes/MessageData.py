from typing import *


class MessageData:
    def __init__(self) -> None:
        self.__data = {}

    async def get_data(self, message_id: int) -> dict:
        return self.__data[message_id]

    async def add_data(self, message_id: int, data: dict):
        self.__data[message_id] = data
