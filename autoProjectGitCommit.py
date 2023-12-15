# {"date":"2023-12-11T12:36:16+01:00"}

import time
import pyautogui
import webbrowser

url = 'https://chat.openai.com/auth/login'

# print(pyautogui.position()) 

class IdeaList:
    def __init__(self):
        self.ideas = [
            "Write a program that prints 'Hello, World!'",
            "Create a simple calculator",
            "Build a basic to-do list application",
            "Implement a program to check if a number is even or odd",
            "Design a program to convert temperatures between Celsius and Fahrenheit",
            "Write a script that generates a random password",
            "Develop a program to find the factorial of a number",
            "Create a basic alarm clock application",
            "Build a program to check if a word is a palindrome",
            "Implement a program to calculate the area of a circle"
        ]

    def add_idea(self, idea):
        self.ideas.append(idea)

    def print_ideas(self):
        print("Ideas:")
        for idea in self.ideas:
            print(f"- {idea}")


webbrowser.open(url)

# click on Login 
pyautogui.moveTo(1400, 550, duration = 0.5)
pyautogui.click()
time.sleep(2)
pyautogui.moveTo(926, 550, duration = 0.5)
pyautogui.click()

# enters Email
pyautogui.typewrite("vier.drei1")
pyautogui.hotkey("ctrl","alt", "q")
pyautogui.typewrite("web.de")
pyautogui.press("enter")

# enter Pw
pyautogui.moveTo(926, 675, duration = 1)
pyautogui.click()
pyautogui.typewrite("python.Auto.Commit.2023")
pyautogui.press("enter")
time.sleep(5)

# ask ChatGPT
pyautogui.moveTo(685, 950, duration = 1)
pyautogui.click()
pyautogui.typewrite("write a code for ")
pyautogui.press("enter")

# string idea = (Calculator, Primnumbers to n, )
# print("write a code for (idea) in python")

# pyautogui.typewrite("vier.drei1@web.de")
# pyautogui.press("enter") 


# pyautogui.click(button="right")

 
