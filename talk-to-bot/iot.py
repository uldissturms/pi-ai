import paho.mqtt.client as mqtt
from urllib.parse import urlparse
from os import getenv

def on_log(client, userdata, level, buf):
    print(client, userdata, level, buf)

def on_connect(client, userdata, flags, rc):
    print('[iot] connected')
    client.subscribe(getenv('MQTT_TOPIC'))

def on_message(client, _, msg):
    print('[iot] message received {}'.format(msg))

def connect(ws_url):
    urlparts = urlparse(ws_url)
    headers = {
        'Host': '{0:s}'.format(urlparts.netloc),
    }
    client = mqtt.Client(transport='websockets')
    client.on_log = on_log
    client.on_connect = on_connect
    client.on_message = on_message

    client.ws_set_options(
        path="{}?{}".format(urlparts.path, urlparts.query),
        headers=headers
    )
    client.tls_set()
    client.connect(urlparts.netloc, 443)
    client.loop_forever()

connect(getenv('MQTT_WS'))
