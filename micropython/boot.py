# This file is executed on every boot (including wake-boot from deepsleep)
import esp
esp.osdebug(None) # turn off vendor O/S debugging messages

import gc
gc.collect()


import esplib
esplib.connectWifi()


# start webrepl
import webrepl
webrepl.start()
