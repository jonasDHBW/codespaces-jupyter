import pyautogui
import time
 
 
time.sleep(2)  
  
dot_loc = pyautogui.locateCenterOnScreen(r'Projekt\buttons\dotsDiscord.png')
bell_loc = pyautogui.locateCenterOnScreen(r'Projekt\buttons\bellDiscord.png')
    
pyautogui.click(dot_loc)
time.sleep(1)
pyautogui.click(bell_loc)

