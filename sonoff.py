# Sonoff board classes

import machine

class Basic:
    """ Sonoff basic class """

    def __init__(self):

        self.led = machine.Pin(13, machine.Pin.OUT)

    def ledOff(self):
        self.led.value(1)

    def ledOn(self):
        self.led.value(0)

    def ledToggle(self):
        self.led.value(1-self.led.value())        
