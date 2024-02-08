import pyautogui
import time

time.sleep(3)

og_width = 1920
og_hight = 1080
    
og_button_X = 248
og_button_Y = 310

def get_user_dimension():
    return pyautogui.size()

def clickOnPoint(x,y, duration=2):
    user_width, user_height = get_user_dimension()
     
    screenRatio_X = user_width/og_width
    screenRatio_Y = user_height/og_hight
    
    user_button = pyautogui.locateOnScreen(r'Projekt\buttons\deleteDotsBright.png')
    user_button_X , user_button_Y = user_button.left, user_button.top

    if og_button_X == user_button_X and og_button_Y == user_button_Y:
        webRatio_X = 1
        webRatio_Y = 1
    else:
        webRatio_X = user_button_X/user_width
        webRatio_Y = user_button_Y/user_height   
    
    var_X = screenRatio_X*webRatio_X
    var_Y = screenRatio_Y*webRatio_Y

    pyautogui.moveTo(x*var_X, y*var_Y, duration=duration)
    pyautogui.click()

clickOnPoint(1400, 542)






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

##### Chat

# import pyautogui
# import time

# time.sleep(3)

# og_width = 1920
# og_height = 1080

# def get_user_dimension():
#     return pyautogui.size()

# def click_on_point(x, y, duration=2):
#     user_width, user_height = get_user_dimension()

#     screen_ratio_x = user_width / og_width
#     screen_ratio_y = user_height / og_height

#     user_button = pyautogui.locateOnScreen(r'Projekt\buttons\deleteDotsBright.png')
    
#     if user_button is not None:
#         user_button_center = pyautogui.center(user_button)
#         user_button_x, user_button_y = user_button_center
#         web_ratio_x = user_button_x / user_width
#         web_ratio_y = user_button_y / user_height

#         var_x = screen_ratio_x * web_ratio_x
#         var_y = screen_ratio_y * web_ratio_y

#         pyautogui.moveTo(x * var_x, y * var_y, duration=duration)
#         pyautogui.click()
#     else:
#         print("Button nicht gefunden.")

# click_on_point(1400, 542)



# import pyautogui
# import time

# def get_screen_dimensions():
#     return pyautogui.size()

# def delete_chat():
#     # Click at multiple positions to delete chat
    
    
#     click_at_position(245, 308)
#     click_at_position(340, 465)
#     click_at_position(1160, 650)

# def click_at_position(x, y, duration=2):
#     screen_width, screen_height = get_screen_dimensions()

#     # Calculate percentages
#     per_width = x / 1920
#     per_height = y / 1080

#     # Calculate the coords 
#     coord_X = screen_width * per_width
#     coords_Y = screen_height * per_height

#     # Move and click
#     pyautogui.moveTo(coord_X, coords_Y, duration=duration)
#     pyautogui.click()

# # time.sleep(3)
# # delete_chat()
# # Corrected code
# screen_dimensions = get_screen_dimensions()
# print(screen_dimensions)
# click_at_position(500, 500)
# print(pyautogui.position()) 
