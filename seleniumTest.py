from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://chat.openai.com/auth/login'

# Initialize the Chrome driver
driver = webdriver.Edge()

try:
    # Maximize the browser window
    driver.maximize_window()

    # Navigate to the URL
    driver.get(url)

    # Wait for the element to be clickable
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div[1]/div/div/button[1]')))

    # Perform the click action using ActionChains (optional)
    # actions = ActionChains(driver)
    # actions.click(element).perform()

    # Click the element
    element.click()

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser window
    driver.quit()


