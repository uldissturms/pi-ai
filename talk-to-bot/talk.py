#!/usr/bin/env python

from os import getenv
import paho.mqtt.client as mqtt
import json
import bot
from time import sleep

TALK_TO_BOT = 'uldis:talk_to_bot'
TELL_BOT = 'uldis:tell_bot'
INTERRUPT = 'uldis:interrupt'

INTENT = TALK_TO_BOT

sessions = {}

def on_connect(client, userdata, flags, rc):
    print('[snips] connected')
    client.subscribe('hermes/intent/#')
    client.subscribe(SESSION_ENDED)

slot_name_is = lambda x: lambda s: s.get('slotName') == x
first_slot_value = lambda s: s.get('value').get('value')

CONTINUE_SESSION = 'hermes/dialogueManager/continueSession'
SESSION_ENDED = 'hermes/dialogueManager/sessionEnded'
SAY = 'hermes/tts/say'

def continue_session(id, text, bot_name):
    return json.dumps({
        'sessionId': id,
        'text': text,
        'intentFilter': [INTERRUPT, TELL_BOT],
        'customData': bot_name,
        'sendIntentNotRecognized': False
    })

def say(text):
    return json.dumps({
        'text': text,
        'siteId': 'default'
    })

def on_continue(client, sessionId, bot_name):
    def inner(response):
        print('[snips] response from bot:', response)
        client.publish(
            CONTINUE_SESSION,
            continue_session(
                sessionId,
                response,
                bot_name
            )
        )
    return inner

def on_message(client, _, msg):
    data = json.loads(msg.payload)
    print(data)
    sessionId = data.get('sessionId')
    intent = data.get('intent')
    intent_name = intent.get('intentName') if intent else None

    if ('termination' in data):
        return on_session_ended(client, sessionId)

    fn = fns.get(intent_name, debug)
    fn(client, sessionId, data)

def on_log(client, userdata, level, buf):
    print('[snips] {}'.format([client, userdata, level, buf]))

def on_session_ended(client, sessionId):
    session = sessions.pop(sessionId)
    if session:
        session.get('client').disconnect()
        bot_name = session.get('name')
        client.publish(
            SAY,
            say('conversation with {} has ended'.format(bot_name))
        )

def on_talk_to_bot(client, sessionId, data):
    slot = next(filter(
        slot_name_is('bot'),
        data.get('slots')
    ))
    bot_name = first_slot_value(slot)

    print('[snips] user wants to talk to {}'.format(bot_name))
    bot_client = bot.start(
        bot_name,
        on_continue(client, sessionId, bot_name)
    )
    sessions[sessionId] = {
        'client': bot_client, 
        'name': bot_name
    }

def debug(a, b, data):
    slots = data.get('slots')
    intent = data.get('intent')
    intent_name = intent.get('intentName') if intent else None
    print('[snips] [debug] Intent {}'.format(intent_name))
    for slot in slots:
        slot_name = slot.get('slotName')
        raw_value = slot.get('rawValue')
        value = slot.get('value').get('value')
        print('[snips] Slot {} -> \n\tRaw: {} \tValue: {}'.format(slot_name, raw_value, value))

fns = {
    TALK_TO_BOT: on_talk_to_bot
}

def start():
    MQTT_HOST = getenv('MQTT_HOST', 'pi')
    MQTT_PORT = getenv('MQTT_PORT', 1883)
    client = mqtt.Client()
    if getenv('DEBUG'):
        client.on_log = on_log
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(MQTT_HOST, MQTT_PORT)
    client.loop_start()
    while True:
        sleep(5)

if __name__ == '__main__':
    print('[snips] starting...')
    start()
