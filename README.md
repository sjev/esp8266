# esp8266
playing with Python on ESP8266 chips, Sonoff &amp; wemos boards



## Preparation
1. get `esptool` from github
2. download 



## Flashing uPython on Sonoff

based on [this tutorial](https://medium.com/cloud4rpi/getting-micropython-on-a-sonoff-smart-switch-1df6c071720a)

1. boot in fw flash mode (hold button during power on)
2. erase flash  `./esptool.py --port /dev/ttyUSB0 erase_flash`
3. boot in fw flash mode
4. flash firmware `esptool.py --port /dev/ttyUSB0 write_flash -fs 1MB -fm dout 0x0 fw/esp8266-20171101-v1.9.3.bin`
5. connect with `picocom /dev/ttyUSB0 -b 115200`


## Flashing uPython on Wemos D1 Pro

see [forum](https://forum.micropython.org/viewtopic.php?f=16&t=2827&start=30#p19737)

1. download custom fw (from [here](https://github.com/micropython/micropython/files/1764650/MicroPython-Firmware-esp8266.zip))
2. erase flash
3. flash with `esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash -fm dio -fs 16MB 0 firmware-combined.bin 0xffc000 esp_init_data_default.bin`


## Toolchain 

* [ampy](https://github.com/adafruit/ampy) - Utility to interact with a MicroPython board over a serial connection.
* picocom - serial terminal

## Rererences

* [MicroPython documentation](https://docs.micropython.org/en/latest/esp8266/index.html)
* [GPIO locations](https://github.com/arendst/Sonoff-Tasmota/wiki/GPIO-Locations)
