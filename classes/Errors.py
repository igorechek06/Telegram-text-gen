from sources import text


class NotGroupOwned(Exception):
    def __init__(self) -> None:
        super().__init__(text.error.NotGroupOwned)


class ArgumentError(Exception):
    def __init__(self) -> None:
        super().__init__(text.error.ArgumentError)
