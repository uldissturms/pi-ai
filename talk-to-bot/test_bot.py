from bot import *

bot_name = 'bot'

def test_start():
    start(bot_name, None, lambda a, b: 'bot speaking')

def test_connect_not_configured():
    assert connect(bot_name, None) == '{} not configured'.format(bot_name)
