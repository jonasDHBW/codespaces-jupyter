# extract the answer
import pyautogui
import webbrowser
import time

from utils import click_right, click_at_position, press_key

    
def clickOnCopy():
    time.sleep(20)
    click_at_position(720, 843)

# xpath = ""

# def open_def_tool():
#     click_right(1560, 680)
#     click_at_position(1250, 650)
  
# def open_search_bar():
#     time.sleep(2)
#     pyautogui.hotkey('Ctrl','Shift','F')
    
# def search_for_button():
#     time.sleep(2)
#     click_at_position(1380, 825)
#     pyautogui.doubleClick()
#     time.sleep(2)
#     pyautogui.hotkey('ctrl','A')
#     pyautogui.hotkey('Delete')
#     pyautogui.doubleClick()
    
# def xpath():
#     pyautogui.typewrite(xpath)
#     press_key("enter")