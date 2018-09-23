from sys import argv
from os import getenv
from hermes_python.hermes import Hermes

MQTT_IP_ADDR=getenv('MQTT_HOST', 'localhost')
MQTT_PORT=getenv('MQTT_PORT', 1883)
MQTT_ADDR='{}:{}'.format(MQTT_IP_ADDR, str(MQTT_PORT))

INTENT_START='uldis:talk_to_bot'
INTENT_INTERRUPT='uldis:interrupt'

INTENT_FILTER_CHAT = [
    INTENT_INTERRUPT
]

msg_start='what would you like to know?'
msg_end='speak soon!'

def user_request_talk_to_bot(hermes, msg):
    bot=msg.slots.bot.first().value
    print('user wants to talk to {}'.format(bot))

    # hermes.publish_continue_session(msg.session_id, msg_start, INTENT_FILTER_CHAT)
    hermes.publish_continue_session(msg.session_id, msg_start, INTENT_FILTER_CHAT)

def user_quits(hermes, msg):
    print('user wants to quit')
    hermes.publish_end_session(msg.session_id, msg_end)

def run():
    with Hermes(MQTT_ADDR) as h:
        h.subscribe_intent(INTENT_START, user_request_talk_to_bot) \
            .subscribe_intent(INTENT_INTERRUPT, user_quits) \
            .start()

if 'run' in argv:
    run()

if 'test' in argv:
    user_request_talk_to_bot()
