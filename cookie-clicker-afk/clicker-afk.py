from pyautogui import *
import pyautogui
import time
import random
import win32api, win32con

while golden_cookie:
  if pyautogui.locateOnScreen('yummy.png', confidence=0.8, grayscale=True) != None:
    print("HOLY SHIT THERE IT IS")
    time.sleep(0.3)
    
  else:
    print("I CAN'T SEE SHIT")
    time.sleep(0.3)