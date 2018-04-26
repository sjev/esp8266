print('Running main.py')
print('network config:', sta_if.ifconfig())

import utime

def buttonPressed(p):
    print('Button pressed ',p)

board.setButtonCallback(buttonPressed)

while True:
    board.ledToggle()
    utime.sleep(1)
    print('.',end='')
