
# used for pyatogui
import time
import pyautogui
import webbrowser

# used for selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
    
# main_script.py
from utils import initialize_driver, navigate_to_url, click_element
from utils import open_browser, perform_login, ask_chat_gpt
from idea import IdeaManager

if __name__ == "__main__":
    url = 'https://chat.openai.com/auth/login'
    open_browser(url)

    im = IdeaManager()

    perform_login()
    ask_chat_gpt(im)
    




 
