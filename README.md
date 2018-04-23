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



## Rererences

* [MicroPython documentation](https://docs.micropython.org/en/latest/esp8266/index.html)
