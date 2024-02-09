from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to your Chrome WebDriver. Download it from https://sites.google.com/a/chromium.org/chromedriver/downloads
chrome_driver_path = '/path/to/chromedriver'

# Initialize Chrome WebDriver
driver = webdriver.Chrome(chrome_driver_path)

# Website URL to navigate
url = 'https://example.com'

# Open the website
driver.get(url)

# Example: Clicking on a button with id "my_button"
try:
    # Wait for the button to be clickable
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'my_button')))
    
    # Click the button
    button.click()

    # You can add more actions here like navigating to another page, filling out forms, etc.

finally:
    # Close the browser window
    driver.quit()
