#!/usr/bin/env python

from os import getenv
import paho.mqtt.client as mqtt
from urllib.parse import urlparse

def on_connect(mqtt_client, userdata, flags, rc):
    print('[bot] connected')
    mqtt_client.subscribe(getenv('BOT_MQTT_TOPIC', '#'))

def on_message(client, _, msg):
    print('[bot] message received {}'.format(msg))

def log(x):
    print('[bot] {}'.format(x))
    return x

def on_log(client, userdata, level, buf):
    log([client, userdata, level, buf])

def connect(bot_name, on_continue):
    [mqtt_client, host, port] = mqtt_client_for(bot_name) or [None, None, None]

    if not mqtt_client:
        log('{} not configured'.format(bot_name))
        return None

    print('[bot] connecting to {}:{}'.format(host, port))

    if getenv('DEBUG'):
        mqtt_client.on_log = on_log

    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.connect(host, port)

    on_continue('bot speaking....')
    mqtt_client.loop_forever()

def mqtt_client_for(bot_name, getenv=getenv):
    bot_name_var = bot_name.upper()

    ws_url = getenv('{}_MQTT_WS'.format(bot_name_var))
    if ws_url:
        mqtt_client = mqtt.Client(transport='websockets')
        urlparts = urlparse(ws_url)
        return [mqtt_client, urlparts.netloc, 443]

    host = getenv('{}_MQTT_HOST'.format(bot_name_var))
    port = getenv('{}_MQTT_PORT'.format(bot_name_var), 1883)

    if host and port:
        mqtt_client = mqtt.Client()
        return [mqtt_client, host, int(port)]

    return None

def start(bot_name, on_continue, connect=connect):
    print('[bot] {} taking over'.format(bot_name))
    connect(bot_name, on_continue)

if __name__ == '__main__':
    print('[bot] starting...')
    start('bot', on_continue=lambda x: log(x))
