# {"date":"2023-12-11T12:36:16+01:00"}

import time
import pyautogui
# print(pyautogui.position()) 

pyautogui.moveTo(205, 1050, duration = 1)
pyautogui.click()

time.sleep(5)

# go to Edge 
pyautogui.moveTo(930, 35, duration = 1) 
pyautogui.click()
pyautogui.moveTo(950, 70, duration = 1) 
pyautogui.click() 

# Open ChatGPT
pyautogui.typewrite("https://chat.openai.com/auth/login")
pyautogui.press("enter") 
time.sleep(5)

# click on Login 
pyautogui.moveTo(1400, 510, duration = 1)
pyautogui.click()
pyautogui.moveTo(926, 481, duration = 1)
pyautogui.click()
pyautogui.typewrite("vier.drei1@web.de")


# pyautogui.typewrite("vier.drei1@web.de")
# pyautogui.press("enter") 


# pyautogui.click(button="right")

 
