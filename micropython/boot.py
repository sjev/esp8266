# This file is executed on every boot (including wake-boot from deepsleep)
import esp
esp.osdebug(None) # turn off vendor O/S debugging messages

import gc
gc.collect()

import sonoff
board = sonoff.Basic()
board.ledOn()


import config

#setup network
import network
sta_if = network.WLAN(network.STA_IF)

ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)
#
if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.active(True)
    sta_if.connect(config.ESSID, config.PASS)
    while not sta_if.isconnected():
        pass
print('network config:', sta_if.ifconfig())

board.ledOff()

# start webrepl
import webrepl
webrepl.start()
