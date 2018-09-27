from bot import *

bot_name = 'bot'

def test_start():
    start(bot_name, None, lambda a, b: 'bot speaking')

def test_connect_not_configured():
    assert connect(bot_name, None) == None

def test_mqtt_client_for_websockets():
    def getenv(x, y=None):
        if x == 'BOT_MQTT_WS':
            return 'ws://some-host'
    [ client, host, port ] = mqtt_client_for(bot_name, getenv)
    assert client._transport == 'websockets'
    assert host == 'some-host'
    assert port == 443

def test_mqtt_client_for_host_and_port():
    def getenv(x, y=None):
        if x == 'BOT_MQTT_HOST':
            return 'some-host'
        if x == 'BOT_MQTT_PORT':
            return 443
    [ client, host, port ] = mqtt_client_for(bot_name, getenv)
    assert client._transport == 'tcp'
    assert host == 'some-host'
    assert port == 443
