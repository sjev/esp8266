"""
Board definitions
"""

# convenience imports
from machine import Pin

class Sonoff:
    """ Sonoff board """

    def __init__(self):

        self.led = Pin(13, Pin.OUT)
        self.button = Pin(0,Pin.IN)

    def ledOff(self):
        self.led.value(1)

    def ledOn(self):
        self.led.value(0)

    def ledToggle(self):
        self.led.value(1-self.led.value())

    def setButtonCallback(self, callback):
        """ add interrupt for button pressed """
        self.button.irq(trigger=Pin.IRQ_FALLING, handler=callback)

