#!/usr/bin/env sh

mosquitto_pub -h pi -t hermes/asr/inject -f injections.json
