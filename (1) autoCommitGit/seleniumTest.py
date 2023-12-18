from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://chat.openai.com/auth/login'

# Initialize the Chrome driver
driver = webdriver.Chrome()

try:
    # Maximize the browser window
    driver.maximize_window()

    # Navigate to the URL
    driver.get(url)

    # login Button
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div[1]/div/div/button[1]')))
    element.click()
    
    # Email 
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div[1]/div/div/button[1]')))
    element.click()

except Exception as e:
    print(f"An error occurred: {e}")

# Do not close the browser in the finally block to keep the tab open
# finally:
#     driver.quit()
