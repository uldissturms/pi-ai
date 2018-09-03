### python

* [spidev](https://pypi.org/project/spidev/) - SPI devices
* [gpiozero](https://pypi.org/project/gpiozero/) - GPIO devices


changing GPIOs

```python
import RPi.GPIO as GPIO
import time

relaypin = 6
GPIO.setmode(GPIO.BCM)
GPIO.setup(relaypin, GPIO.OUT)
GPIO.output(relaypin, GPIO.HIGH)
time.sleep(10.0)
GPIO.output(relaypin, GPIO.LOW)
```
