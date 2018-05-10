print('Running main.py')

import time
import config

while True:
    config.board.ledToggle()
    time.sleep(1)