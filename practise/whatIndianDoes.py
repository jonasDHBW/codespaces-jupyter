import pyautogui
import time

def getDots():
    dots = pyautogui.locateCenterOnScreen(r'Projekt\buttons\dotsDiscord.png')
        
    pyautogui.moveTo(dots)
    pyautogui.click()


def getBell():
    bell = pyautogui.locateCenterOnScreen(r'Projekt\buttons\bellDiscord.png')
    
    pyautogui.moveTo(bell)
    pyautogui.click()


time.sleep(3)
getDots()
time.sleep(3)
getBell()