text=$@
mosquitto_pub -h pi -t 'hermes/tts/say' -m "{\"text\": \"$text\", \"siteId\": \"default\"}"

