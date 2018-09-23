from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

ca_certs = './certs/AmazonRootCA1.pem'
certfile = './certs/xxx-certificate.pem.crt'
keyfile = './certs/xxx-private.pem.key'

# For certificate based connection
# myMQTTClient = AWSIoTMQTTClient("xxx")
# For Websocket connection
myMQTTClient = AWSIoTMQTTClient("xxx", useWebsocket=True)
# Configurations
# For TLS mutual authentication
# myMQTTClient.configureEndpoint("xxx.iot.eu-west-1.amazonaws.com", 8883)
# For Websocket
myMQTTClient.configureEndpoint("xxx.iot.eu-west-1.amazonaws.com", 443)
# For TLS mutual authentication with TLS ALPN extension
# myMQTTClient.configureEndpoint("YOUR.ENDPOINT", 443)
# myMQTTClient.configureCredentials(ca_certs, keyfile, certfile)
# For Websocket, we only need to configure the root CA
myMQTTClient.configureCredentials(ca_certs)
myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

myMQTTClient.connect()
myMQTTClient.publish("test-iot", "python speaking", 0)
myMQTTClient.disconnect()
