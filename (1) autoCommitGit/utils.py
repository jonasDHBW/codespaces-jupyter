# utils.py
import pyautogui
import webbrowser
import time

# selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# pyautogui
from idea_manager import IdeaManager

# def initialize_driver():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     return driver

# def navigate_to_url(driver, url):
#     driver.get(url)

# def click_element(driver, xpath):
#     wait = WebDriverWait(driver, 10)
#     element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
#     element.click()

def open_browser(url):
    webbrowser.open(url)

def click_at_position(x, y, duration=0.5):
    pyautogui.moveTo(x, y, duration=duration)
    pyautogui.click()

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

def ask_chat_gpt(idea_manager):
    click_at_position(685, 950, duration=1)
    
    # Lade die Ideen
    ideas = idea_manager.load_ideas()

    # Verwende die erste Idee, wenn vorhanden
    if ideas:
        pyautogui.typewrite(f"write a code for {ideas[0]} in python")
        press_key("enter")
    else:
        print("No ideas available.")
