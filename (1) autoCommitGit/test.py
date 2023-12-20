# utils.py
import pyautogui
import webbrowser
import time

# selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://chat.openai.com/auth/login'  # Replace with the actual URL
button_xpath = '/html/body/div[1]/div[1]/div[2]/div[1]/div/div/button[1]'  # Replace with the actual XPath of the button

options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

def initialize_driver():
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver

def navigate_to_url(driver, url):
    time.sleep(3)
    driver.get(url)

# def click_button_by_xpath(driver, button_xpath):
#     button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
#     button.click()
    
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

if __name__ == "__main__":
    driver = initialize_driver()
    navigate_to_url(driver, url)
    
    # Click on the button using its XPath
    # click_button_by_xpath(driver, button_xpath)
    
    # perform_login()
    time.sleep(2)
    click_at_position(1400, 550)
    time.sleep(2)
    click_at_position(940, 500)
    # Close the browser window

# perfomrInPowerShell

# C:/Python312/python.exe "c:/Users/jpl/VS Code for Git/codespaces-jupyter/seleniumTest.py"


