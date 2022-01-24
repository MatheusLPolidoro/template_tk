from pyautogui import *

def teste():
    moveTo(100, 150)
    moveTo(400, 0)  
    moveTo(500, 500, duration=2, tween=easeInOutQuad)
