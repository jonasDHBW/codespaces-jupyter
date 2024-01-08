

import undetected_chromedriver as uc
from selenium import webdriver

options = webdriver.ChromeOptions()
# options.headless = False
# options.add_argument("start-maximized")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
driver = uc.Chrome(options = options)
driver.get('https://chat.openai.com/auth/login')


# https://pypi.org/project/undetected-chromedriver/
# https://stackoverflow.com/questions/68289474/selenium-headless-how-to-bypass-cloudflare-detection-using-selenium


