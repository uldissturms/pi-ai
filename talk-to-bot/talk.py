# !/usr/bin/env python
# encoding: utf-8

from os import getenv
import paho.mqtt.client as mqtt
import json
import bot

MQTT_HOST = getenv('MQTT_HOST', 'localhost')
MQTT_PORT = getenv('MQTT_PORT', 1883)
mqtt_client = mqtt.Client()

TALK_TO_BOT = 'uldis:talk_to_bot'
INTERRUPT = 'uldis:interrupt'

INTENT = TALK_TO_BOT

def on_connect(client, userdata, flags, rc):
    print('[snips] connected')
    mqtt_client.subscribe('hermes/intent/{}'.format(INTENT))
    # mqtt_client.subscribe('hermes/dialogueManager/sessionEnded')

slot_name_is = lambda x: lambda s: s['slotName'] == x
first_slot_value = lambda s: s['value']['value']

CONTINUE_SESSION = 'hermes/dialogueManager/continueSession'

CONTINUE_SESSION_MSG = 'mkay'

def continue_session(id, text, bot_name):
    return json.dumps({
        'sessionId': id,
        'text': text,
        'intentFilter': [INTERRUPT],
        'customData': bot_name,
        'sendIntentNotRecognized': False
    })

def on_message(client, _, msg):
    data = json.loads(msg.payload)
    intent_name = data['intent']['intentName']
    sessionId = data['sessionId']

    if (intent_name == TALK_TO_BOT):
        slot = filter(
            slot_name_is('bot'),
            data['slots']
        )[0]
        bot_name = first_slot_value(slot)

        print('[snips] user wants to talk to {}'.format(bot_name))
        response = bot.start(bot_name)
        mqtt_client.publish(
            CONTINUE_SESSION,
            continue_session(
                sessionId,
                response,
                bot_name
            )
        )
    else:
        debug(data)

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
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.connect('pi', 1883)
    mqtt_client.loop_forever()

if __name__ == '__main__':
    print('[snips] starting...')
    start()
