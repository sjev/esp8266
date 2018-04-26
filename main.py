print('Running main.py')
print('network config:', sta_if.ifconfig())

import utime


while True:
    board.ledToggle()
    utime.sleep(1)
    print('.',end='')
