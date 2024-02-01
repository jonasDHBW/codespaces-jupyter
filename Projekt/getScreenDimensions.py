import pyautogui

# Dimension of your Screen
def getDimensions():
    
    screenWidth, screenHeight = pyautogui.size()  
    return screenWidth, screenHeight

# calculates the percentage of an 1920/1024 Screen
def calculatePercentage():
    screenWidht, screenHeight= getDimensions()  
    perW = x / 1920
    perH = y / 1024
    return perW, perH

# calculates in what relation the op screen an your screen stand
def calculateVariable():
    screenWidht, screenHeight= getDimensions()
    vX = screenWidht/1920
    vY = screenHeight/1024
    return vX, vY

# get stuff
screenWidht, screenHeight = getDimensions()
perW, perH = calculatePercentage()
vX, vY = calculateVariable()

print(perW, perH)
    
# get the right button for everybody 
pyautogui.click(screenWidht*perW*vX, screenHeight*perH*vY)  
print(screenWidht*perW, screenHeight*perH)
print(pyautogui.position()) 