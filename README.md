# esp8266
playing with Python on ESP8266 chips, Sonoff &amp; wemos boards



## Preparation
1. Clone this directory
2. run `INIT` to install python dependencies and init submodules




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
* [TH10 jack pinout](http://tinkerman.cat/sonoff-th10-th16-sensors-displays-actuators/#lightbox-gallery-F3O8/8/)

### temperature sensing
The sensor supplied with TH10 is DS18B20 . Opitonal is AM2301.
To read DS18B20, use [ds18x20.py](https://github.com/micropython/micropython/blob/master/drivers/onewire/ds18x20.py) module. A reference for usagecan be found in older [docs](http://docs.micropython.org/en/v1.8.2/esp8266/esp8266/tutorial/onewire.html)



### git
 * [git submodules](https://stackoverflow.com/questions/2140985/how-to-set-up-a-git-project-to-use-an-external-repo-submodule)
 * [ignore changes](https://content.pivotal.io/blog/ignoring-tracked-files-in-git)
