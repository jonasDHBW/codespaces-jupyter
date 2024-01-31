# utils.py
import pyautogui
import webbrowser
import time

def getDimensions():
        screenWidth, screenHeight = pyautogui.size()  # Get the size of the primary monitor.
        return screenWidth, screenHeight

def open_browser(url):
    webbrowser.open(url)
    
def close_browser():
    pyautogui.press('ctrl' + 'w')

def click_at_position(x, y, duration=0.5):

    def calculatePercentage():
        screenWidht, screenHeight= getDimensions()  # Call the getDimensions function to get screen dimensions
        perW = x / screenWidht
        perH = y / screenHeight
        return perW, perH

    screenWidht, screenHeight = getDimensions()
    perW, perH = calculatePercentage()
        
    pyautogui.moveTo(screenWidht*perW, screenHeight*perH, duration=duration)  
    pyautogui.click()

def click_right(x, y, duration=0.5):
    pyautogui.moveTo(x, y, duration=duration)
    pyautogui.rightClick()
    
def type_with_shortcut(text, shortcut):
    pyautogui.typewrite(text)
    pyautogui.hotkey(*shortcut)

def press_key(key):
    pyautogui.press(key)

def perform_login():
    time.sleep(2)
    click_at_position(1400, 550)
    time.sleep(2)
    click_at_position(926, 550)

    type_with_shortcut("vier.drei1", ["ctrl", "alt", "q"])
    pyautogui.typewrite("web.de")
    press_key("enter")

    click_at_position(926, 675, duration=1)
    pyautogui.typewrite("python.Auto.Commit.2023")
    press_key("enter")
    time.sleep(5)

def ask_chat_gpt(ideas):
    click_at_position(685, 950, duration=1)

    # Verwende die erste Idee, wenn vorhanden
    if ideas:
        pyautogui.typewrite("write a code in python for " + ideas)
        press_key("enter")
    else:
        print("No ideas available.")
        
def copy_discussion():
    click_at_position()
    
def clickOnCopy():
    time.sleep(20)
    click_at_position(720, 843)
    time.sleep(2)
