import pyautogui


def get_user_dimension():
    return pyautogui.size()

def ask_user():
    while True:
        print("Do you use Chrome or Edge? Answer with C or E")
        answer = input("Your choice (C or E): ").upper()

        if answer == "C" or answer == "E":
            return answer
        else:
            print("Invalid input. Please answer with C or E. Try again.")

def calculate_website_coordinates(user_choice):
    user_width, user_height = get_user_dimension()

    if user_choice == "C":
        # Chrome coordinates
        x_top_left, y_top_left = 0, 150
        x_bottom_right, y_bottom_right = 1920, 1020
        
        # actual website field
        x_browser_lenght, y_browser_lenght = 1920, 1080-(1080-y_bottom_right)-y_top_left 
        
        # variable innerhalb des website-fields
        x_add_perc, y_add_perc = 0, (y_top_left / user_height) * 100

    elif user_choice == "E":
        # Edge coordinates
        x_top_left, y_top_left = 5, 90
        x_bottom_right, y_bottom_right = 1915, 1020
        
        # actual website field
        x_browser_lenght, y_browser_lenght = 1920-(x_top_left)-(1920-x_bottom_right), 1080-(1080-y_bottom_right)-y_top_left
        
        # variable innerhalb des website-fields
        x_add_perc, y_add_perc = (x_top_left / user_width) * 100, (y_top_left / user_height) * 100

    return x_top_left, y_top_left, x_bottom_right, x_browser_lenght, y_browser_lenght, y_bottom_right, x_add_perc, y_add_perc

def click_in_(x, y, duration=2):
    add_X, add_Y, = calculate_website_coordinates()
    
    
    pyautogui.moveTo(add_X + (x * var_x), add_Y + (y * var_y), duration=duration)
    pyautogui.click()

# # Example usage:
# user_choice = ask_user()
# x_tl, y_tl, x_br, y_br, x_perc, y_perc = calculate_website_coordinates(user_choice)
# print(f"Top left coordinates: ({x_tl}, {y_tl})")
# print(f"Bottom right coordinates: ({x_br}, {y_br})")
# print(f"Additional percentages: ({x_perc}%, {y_perc}%)")

    # x_website_field = user_width
    # y_website_field = user_height - y_top_left - (user_height - y_bottom_right)

    # return x_website_field, y_website_field



