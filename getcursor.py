import logging
import time
import  pyautogui
import PIL.ImageGrab

logging.basicConfig(encoding='utf-8', level=logging.DEBUG)


while True: 
    currentMouseX, currentMouseY = pyautogui.position()
    # px = ImageGrab.grab().load()
    # for y in range(0, currentMouseY):
    #     for x in range(0, currentMouseX):
    #         color = px[x, y]
    rgb = PIL.ImageGrab.grab().load()[currentMouseX,currentMouseY]
    logging.debug("X: " + str(currentMouseX) + " Y: " + str(currentMouseY))
    logging.debug("Current Color: " + str(rgb))
    time.sleep(2.0)
