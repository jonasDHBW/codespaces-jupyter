# utils.py
import pyautogui
import webbrowser
import time

def get_screen_dimensions():
    return pyautogui.size()

def open_browser(url):
    webbrowser.open(url)
    click_at_position(721, 842)
    
def close_browser():
    pyautogui.press('ctrl' + 'w')
    
def deleteChat():
    # y-Wert startet von Oben
    click_at_position(245, 308)
    click_at_position(340, 465)
    click_at_position(1160, 650)

def click_at_position(x, y, duration=2):
    screen_width, screen_height = get_screen_dimensions()

    # Calculate percentages
    per_width = x / 1920
    per_height = y / 1080

    # Calculate screen dimension ratios
    ratio_width = screen_width / 1920
    ratio_height = screen_height / 1080
    
    # Calculate the coords 
    coord_X = screen_width * per_width * ratio_width
    coords_Y = screen_height * per_height * ratio_height

    # Move and click
    pyautogui.moveTo(coord_X, coords_Y, duration=duration)
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
    
def clickOnCopy():
    time.sleep(20)
    click_at_position(720, 843)
    time.sleep(2)

def open_discord():
    discord_icon = pyautogui.locateCenterOnScreen('discord_icon.png')  
    if discord_icon:
        pyautogui.click(discord_icon)
    else:
        print("Discord Icon nicht gefunden.")
