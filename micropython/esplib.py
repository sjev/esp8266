
"""
micropython library for ESP8266


"""
import config

import machine
import network
import time

board = config.board

def connectWifi(networks=config.networks):
    """ connect to a wifi network """
    board.ledOn()
    
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(False) # disable access point
    
    sta_if = network.WLAN(network.STA_IF)
    
    if not sta_if.isconnected():
        for essid,password in networks:
            print('connecting to ',essid)
            sta_if.active(True)
            sta_if.connect(essid, password)
            for retry in range(5):
                if sta_if.isconnected():
                    break
                else:
                    print('Retrying #',retry)
                    time.sleep(1)
            if sta_if.isconnected():
                    break
    
    if sta_if.isconnected(): # should be connected now
        print('network config:', sta_if.ifconfig())
        board.ledOff()
    else: # warn with led and reboot
        for i in range(10):
            board.led.toggle()
            time.sleep_ms(200)
        print('Restarting')
        machine.reset()
        
               
        



