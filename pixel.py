import PIL.ImageGrab
import logging
import time

logging.basicConfig(encoding='utf-8', level=logging.DEBUG)


import time
#X,Y
# (455, 301)
# 198 366
# Range
dannygreen=(199, 203)
pixelX=648
pixelY=226
# px = ImageGrab.grab().load()
# for y in range(0, 301, 10):
#     for x in range(0, 455, 10):
#         color = px[x, y]
while True: 
    rgb = PIL.ImageGrab.grab().load()[pixelX,pixelY]
    logging.debug('Finding Game...')
    logging.debug("Current Color: " + str(rgb))
    time.sleep(2.0)
    if (rgb[0] != dannygreen[0] and rgb[1] != dannygreen[1] ):
        logging.debug('Game Found!')
        break

logging.debug('Starting Countdown to Quit Game...')
