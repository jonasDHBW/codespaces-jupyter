# import pyautogui

# print(pyautogui.position()) 



# pip install pyscreeze==0.1.27
# pip install Pillow 

import pyautogui
import time

time.sleep(3)
start = pyautogui.locateOnScreen(r'Projekt\images\logInButton.png')#If the file is not a png file it will not work
print(start)
pyautogui.moveTo(start)#Moves the mouse to the coordinates of the image