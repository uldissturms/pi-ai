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

def start(name):
    print('[bot] {} taking over'.format(name))
    bot = name.upper()

    host = getenv('{}_MQTT_HOST'.format(bot))
    port = getenv('{}_MQTT_PORT'.format(bot))

    if not host:
        return log('{} not configured'.format(name))

    print('[bot] connecting to {}:{}'.format(host, port))
    mqtt_client = mqtt.Client()
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message

    return log('{} speaking...'.format(name))
