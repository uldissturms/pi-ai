#!/usr/bin/env python

from os import getenv
import paho.mqtt.client as mqtt
import json
import bot

TALK_TO_BOT = 'uldis:talk_to_bot'
INTERRUPT = 'uldis:interrupt'

INTENT = TALK_TO_BOT

def on_connect(client, userdata, flags, rc):
    print('[snips] connected')
    client.subscribe('hermes/intent/{}'.format(INTENT))

slot_name_is = lambda x: lambda s: s['slotName'] == x
first_slot_value = lambda s: s['value']['value']

CONTINUE_SESSION = 'hermes/dialogueManager/continueSession'

def continue_session(id, text, bot_name):
    return json.dumps({
        'sessionId': id,
        'text': text,
        'intentFilter': [INTERRUPT],
        'customData': bot_name,
        'sendIntentNotRecognized': False
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
    intent_name = data['intent']['intentName']
    sessionId = data['sessionId']

    if (intent_name == TALK_TO_BOT):
        slot = next(filter(
            slot_name_is('bot'),
            data['slots']
        ))
        bot_name = first_slot_value(slot)

        print('[snips] user wants to talk to {}'.format(bot_name))
        bot.start(
            bot_name,
            on_continue(client, sessionId, bot_name)
        )
    else:
        debug(data)

def on_log(client, userdata, level, buf):
    print('[snips] {}'.format([client, userdata, level, buf]))

def debug(data):
    slots = data['slots']
    intent_name = data['intent']['intentName']
    print('[snips] Intent {}'.format(intent_name))
    for slot in slots:
        slot_name = slot['slotName']
        raw_value = slot['rawValue']
        value = slot['value']['value']
        print('[snips] Slot {} -> \n\tRaw: {} \tValue: {}'.format(slot_name, raw_value, value))

def start():
    MQTT_HOST = getenv('MQTT_HOST', 'pi')
    MQTT_PORT = getenv('MQTT_PORT', 1883)
    client = mqtt.Client()
    if getenv('DEBUG'):
        client.on_log = on_log
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(MQTT_HOST, MQTT_PORT)
    client.loop_forever()

if __name__ == '__main__':
    print('[snips] starting...')
    start()
