class system:
    class patterns:
        select = r"^(?P<prefix>sel_)(?P<id>-[1-9][0-9]*)$"
        set_value = {
            int: r"^[1-9][0-9]*$",
            str: r".+"
        }


class error:
    NotGroupOwned = "⚠ У вас нет групп"
    ArgumentError = "⚠ Неверный аргумент"
    errors = [
        NotGroupOwned,
        ArgumentError
    ]


class group:
    start = "Я выслал создателю этой группы насройки\n" +\
            "—— ℹ После настройки я буду работать"

    owner_not_found = "⚠ Создатель группы не найден \n" +\
                      "ℹ Может быть анонимным \n" +\
                      "Если возникли проблемы @igorechek06"

    owner_not_start = "⚠ Создатель группы ({}) не начал общение с ботом @TGen_bot"


class private:
    start = "Типа start text"

    invited = "Привет, прежде чем начать нужно настроить канал \n"

    class settings:
        select = "Выберете чат для настройки"

        set_value = {
            int: "Введите число",
            str: "Введите строку"
        }

        settings = "Настройки┃@{}┃⚙ \n" +\
                   "🔤 Использовать общедоступную базу - {}  \n" +\
                   "💬 Шанс генерации сообщения (1 - 75) - {}% \n" +\
                   "💬 Упоминание (@username) - {}  \n" +\
                   "💬 Генерировать мемы - {}"

        settings_default = {
            "openGen": False,
            "percent": 10,
            "ping": True,
            "memGen": True
        }
