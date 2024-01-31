import pyautogui

x = 721
y = 842

def getDimensions():
    screenWidth, screenHeight = pyautogui.size()  # Get the size of the primary monitor.
    return screenWidth, screenHeight

def calculatePercentage():
    screenWidht, screenHeight= getDimensions()  # Call the getDimensions function to get screen dimensions
    perW = x / screenWidht
    perH = y / screenHeight
    return perW, perH

def 

screenWidht, screenHeight = getDimensions()
perW, perH = calculatePercentage()

print(perW, perH)
    
pyautogui.click(screenWidht*perW, screenHeight*perH)  
print(screenWidht*perW, screenHeight*perH)
