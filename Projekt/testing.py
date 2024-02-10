import time
import pyautogui

def clickOnSortBy():
    while True:
        sortBy = pyautogui.locateCenterOnScreen(r'Projekt\buttons\sortByGIT.png')
        
        if sortBy is not None:
            pyautogui.moveTo(sortBy)
            pyautogui.click
            print("sortBy found!")
            break  
        else:
            print("sortBy not found")
            
time.sleep(2)
clickOnSortBy()