import optparse

from aiogram import executor, types

import config

parser = optparse.OptionParser(conflict_handler="resolve")
parser.add_option('-t', '--test',
                  action="store_true",
                  dest='test',
                  help='test token')
parser.add_option('-m', '--main',
                  action="store_true",
                  dest='main',
                  help='main token')
values, args = parser.parse_args()

if values.test:
    config.token = config.token_test
elif values.main:
    config.token = config.token_main
else:
    raise ValueError("АРГУМЕНТЫ СУКА")

if True:
    from bot import dp
    import sources

if __name__ == "__main__":
    executor.start_polling(dp)
