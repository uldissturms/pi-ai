### hardware requirements

* raspberry pi (e.g., [ABOX RPi3B Plus starter kit](https://www.amazon.co.uk/gp/product/B07DB8591S/))
* mic array (e.g., [ReSpeaker 4-Mic array](https://shop.pimoroni.com/products/respeaker-4-mic-array-for-raspberry-pi))

### software requirements

* latest version of [raspbian](https://www.raspberrypi.org/downloads/raspbian/)
* [echer](https://etcher.io/) to burn image

### boot - for lite version (no desktop)

* `wpa_supplicant.conf` - WIFI setup on boot

  ```ini
  ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
  network={
      ssid="YOUR_NETWORK_NAME"
      psk="YOUR_PASSWORD"
      key_mgmt=WPA-PSK
  }
  ```

* `touch ssh` - enables ssh on Pi

### hardware setup

* setup ReSpeaker array http://wiki.seeedstudio.com/ReSpeaker_4_Mic_Array_for_Raspberry_Pi/
* testing the mic:
  * `arecord --device=hw:1,0 --format S32_LE -V mono -c 4 test.wav` - record
  * `aplay test.wav` - play
  * tip: these commands can be piped as well `arecord | aplay`
* `alsamixer` - adjust the volume

### sound card setup

mic doesn't work by default, two options:

* uninstall pulseaudio
* update defaults to correct card
  ```
    # cat /etc/pulse/default.pa
    load-module module-alsa-sink device=hw:0,0
    load-module module-alsa-source device=hw:0,0
  ```

### snips setup

* follow instructions on snips installatin page: https://snips.gitbook.io/getting-started/installation

### utils

* `sudo raspi-config` - alter Pi config

### extra

* lights support for ReSpeaker

```
sudo apt-get install portaudio19-dev
```
