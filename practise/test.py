# from selenium import webdriver

# # Specify the path to your ChromeDriver executable
# chrome_driver_path = '/path/to/chromedriver'

# # Create a new instance of the Chrome driver
# driver = webdriver.Chrome(executable_path=chrome_driver_path)

# # URL of the website you want to open
# website_url = 'https://www.example.com'

# # Open the website
# driver.get(website_url)

# # Optionally, you can add a delay to wait for the page to load
# # import time
# # time.sleep(5)  # Wait for 5 seconds

# # Close the browser window
# # driver.quit()
import pyautogui
import time

def get_screen_dimensions():
    return pyautogui.size()

def delete_chat():
    # Click at multiple positions to delete chat
    
    
    click_at_position(245, 308)
    click_at_position(340, 465)
    click_at_position(1160, 650)

def click_at_position(x, y, duration=2):
    screen_width, screen_height = get_screen_dimensions()

    # Calculate percentages
    per_width = x / 1920
    per_height = y / 1080

    # Calculate the coords 
    coord_X = screen_width * per_width
    coords_Y = screen_height * per_height

    # Move and click
    pyautogui.moveTo(coord_X, coords_Y, duration=duration)
    pyautogui.click()

# time.sleep(3)
# delete_chat()
# Corrected code
screen_dimensions = get_screen_dimensions()
print(screen_dimensions)
click_at_position(500, 500)
print(pyautogui.position()) 
