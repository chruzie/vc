import pydirectinput
import time
import logging
import pydirectinput
import PIL.ImageGrab


logging.basicConfig(encoding='utf-8', level=logging.DEBUG)

# 2560x1440
dannygreen=(387, 308)
pixelX=595
pixelY=479


def psButton():
    # PSButton Location = (647, 670)
    pydirectinput.click(600, 600)
    time.sleep(2.0)
    pydirectinput.moveTo(647, 670)
    pydirectinput.doubleClick()
    time.sleep(2.0)
    # logging.debug('Pressing Right')
    # pydirectinput.press('right')
    # time.sleep(2.0)
    logging.debug('Pressing Play Now')
    pydirectinput.press('enter')
    time.sleep(2.0)
    # Enter - Wait 3 (Play Online Now)
    logging.debug('Pressing Resume Activity')
    pydirectinput.press('enter')
    time.sleep(2.0)

counter = 0

# Start Program
logging.debug('Vince Carter Generator Started...')
pydirectinput.click(600, 670)

try:
    while True:
        logging.debug("Starting Loop.Run Count:" + str(counter))
        # PS Button
        logging.debug('Pressing PSButton')
        psButton()
        
        #Right
        logging.debug('Pressing Right')
        pydirectinput.press('right')
        time.sleep(2.0)

        #Right
        logging.debug('Pressing Right')
        pydirectinput.press('right')
        time.sleep(2.0)

        # Enter (Play)
        logging.debug('Pressing PlayNow Online')
        pydirectinput.press('enter')
        time.sleep(2.0)

        # Enter - Wait 2
        pydirectinput.press('enter')
        time.sleep(2.0)

        # Enter (Selecting Tier)
        pydirectinput.press('enter')
        time.sleep(3.0)

        #####################
        # # TIER COMPLETE
        # pydirectinput.press('enter')
        # #Down
        # logging.debug('Pressing Down')
        # pydirectinput.press('down')
        # time.sleep(2.0)
        # # Enter (Selecting Tier)
        # pydirectinput.press('enter')
        # time.sleep(2.0)
        #####################


        # Enter (Team Control)
        pydirectinput.press('enter')
        time.sleep(3.0)

        # Enter -  (Team Select) Wait 10
        logging.debug('Selecting Team')
        pydirectinput.press('enter')
        pydirectinput.press('enter')

        # # Check if game found
        # while True: 
        #     rgb = PIL.ImageGrab.grab().load()[pixelX,pixelY]
        #     logging.debug('Finding Game...')
        #     logging.debug("Current Color: " + str(rgb))
        #     time.sleep(2.0)
        #     if (rgb[0] > 30 and rgb[1] > 30 ):
        #         logging.debug('Game Found!')
        #         logging.debug("Current Color: " + str(rgb))
        #         break

        # logging.debug(' GameCountdown Started...')  
        # logging.debug("Current Color: " + str(rgb))      
        time.sleep(15.0)

        # PS Button
        logging.debug('Quitting Game.')
        #Increment Count
        counter +=1

except KeyboardInterrupt:
    logging.warning('interrupted!')
    logging.info("Congrats you have earned:" + str(counter * 400) + " VC")



# Restart from top


