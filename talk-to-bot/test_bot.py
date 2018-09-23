from bot import *

# def test_start_configured():
#     assert start('bot') == 'bot speaking...'

def test_start_not_configured():
    assert start('bot') == 'bot not configured'
