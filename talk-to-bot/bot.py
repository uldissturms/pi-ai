from os import getenv
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print('[bot] connected')
    mqtt_client.subscribe('#')

def on_message(client, _, msg):
    print('[bot] message received {}'.format(msg))

def log(x):
    print('[bot] {}'.format(x))
    return x

def connect(bot_name, on_continue):
    bot_name_var = bot_name.upper()
    host = getenv('{}_MQTT_HOST'.format(bot_name_var))
    port = getenv('{}_MQTT_PORT'.format(bot_name_var))

    if not host:
        return log('{} not configured'.format(bot_name))

    print('[bot] connecting to {}:{}'.format(host, port))
    mqtt_client = mqtt.Client()
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.connect(host, port)

    on_continue('bot speaking....')

def start(bot_name, on_continue, connect=connect):
    print('[bot] {} taking over'.format(bot_name))
    connect(bot_name, on_continue)
