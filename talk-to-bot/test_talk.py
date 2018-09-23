from talk import *
import json

# {u'customData': None, u'sessionId': u'63317874-1f69-4b6a-8bba-960398df6d7c', u'siteId': u'default', u'input': u'talk to bot', u'slots': [{u'slotName': u'bot', u'range': {u'start': 8, u'end': 11}, u'rawValue': u'bot', u'value': {u'kind': u'Custom', u'value': u'bot'}, u'entity': u'bot'}], u'intent': {u'intentName': u'uldis:talk_to_bot', u'probability': 1.0}}

def test_slot_name_is():
    slot = {'slotName': 'bot'}
    assert slot_name_is('bot')(slot) == True

def test_fist_slot_value():
    slot = {'value': {'value': 'bot'}}
    assert first_slot_value(slot) == 'bot'

def test_continue_session():
    sessionId = 'some-id'
    bot = 'some-bot'
    text = 'some-text'
    msg = continue_session(sessionId, text, bot)
    data = json.loads(msg)
    assert data['sessionId'] == sessionId
    assert data['customData'] == bot
    assert data['text'] == text

