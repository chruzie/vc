import pydirectinput
import time
import logging
import pydirectinput


logging.basicConfig(encoding='utf-8', level=logging.DEBUG)

def psButton():
    # PSButton Location = (647, 670)
    pydirectinput.click(600, 600)
    time.sleep(1.0)
    pydirectinput.moveTo(647, 670)
    pydirectinput.doubleClick()
    time.sleep(1.0)

counter = 0

# Start Program
logging.debug('Vince Carter Generator Started...')
pydirectinput.click(600, 670)

try:
    while True:
        logging.debug("Starting Loop.Run Count:" + str(counter))
        time.sleep(5.0)

        # PS Button
        logging.debug('Pressing PSButton')
        psButton()
        
        # Right
        # logging.debug('Pressing Right')
        # pydirectinput.press('right')
        # time.sleep(1.0)

        # Right
#        logging.debug('Pressing Right')
#        pydirectinput.press('right')
#        time.sleep(1.0)
        logging.debug('Pressing Play Now')
        pydirectinput.press('enter')
        time.sleep(2.0)
        # Enter - Wait 3 (Play Online Now)
        logging.debug('Pressing Resume Activity')
        pydirectinput.press('enter')
        time.sleep(2.0)

        #Right
        logging.debug('Pressing Right')
        pydirectinput.press('right')
        time.sleep(0.5)

        #Right
        logging.debug('Pressing Right')
        pydirectinput.press('right')
        time.sleep(0.5)

        # Enter (Play)
        logging.debug('Pressing PlayNow Online')
        pydirectinput.press('enter')
        time.sleep(1.0)

        # Enter - Wait 2
        pydirectinput.press('enter')
        time.sleep(2.0)

        # Enter (Selecting Tier)
        pydirectinput.press('enter')
        time.sleep(3.0)

        # Enter (Team Control)
        pydirectinput.press('enter')
        time.sleep(3.0)

        # Enter -  (Team Select) Wait 10
        logging.debug('Selecting Team')
        pydirectinput.press('enter')
        pydirectinput.press('enter')

        # Check if game found
        # Loop until pixel at (455, 301) (Color Yellow (229, 218, 16)) is found. Quit game after found.

        time.sleep(15.0)

        # PS Button
        logging.debug('Quitting Game.')
        psButton()

        # Enter
        pydirectinput.press('enter')
        time.sleep(1.0)
        # Enter
        pydirectinput.press('enter')

        #Increment Count
        counter +=1

except KeyboardInterrupt:
    logging.warning('interrupted!')
    logging.info("Congrats you have earned:" + str(counter * 400) + " VC")



# Restart from top


