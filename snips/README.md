### snips

### [hermes protocol](https://snips.gitbook.io/documentation/ressources/hermes-protocol)

used to communicate over MQTT

### actions

https://snips.gitbook.io/documentation/console/actions

### skills

`sam install skills -g https://github.com/snipsco/snips-skill-respeaker.git` - respeaker led lights

### voices

`apt-get install snips-makers-tts`

### say something

* `mosquitto_pub -t 'hermes/tts/say' -m '{"text": "hello sir", "siteId": "default"}'` - post to say topic

note: siteId is required

### debug

* `mosquitto_sub -t 'hermes/intent/[intent_name]'` - listen to intents

  example: `mosquitto_sub -t 'hermes/intent/uldis:talk_to_bot'
  {"sessionId":"3191e707-dc70-45a5-80ba-8250872e38fc","customData":null,"siteId":"default","input":"talk to bot","intent":{"intentName":"uldis:talk_to_bot","probability":1.0},"slots":[{"rawValue":"bot","value":{"kind":"Custom","value":"bot"},"range":{"start":8,"end":11},"entity":"bot","slotName":"bot"}]}`

### troubleshoot

* look in `/var/log/syslog`
* check `_snips` user groups (audio, pulse-access, etc.)

### links

* [Awesome snips](https://github.com/snipsco/awesome-snips)
* [MQTT lib for python](https://pypi.org/project/paho-mqtt)
* [Connect to MQTT](https://snips.gitbook.io/documentation/console/actions/code-your-action/manual-action)
