import time
import pyautogui

def clickOnSortBy():
    copySymbol = pyautogui.locateCenterOnScreen(r'Projekt\buttons\copySymbolChat.png')
        
    if copySymbol is not None:
        pyautogui.moveTo(copySymbol)
        pyautogui.click()
        print("copied the comment!")
    else:
        print("couldn't copy the comment")
    print("ask Chat succesfully!")
            
time.sleep(2)
clickOnSortBy()