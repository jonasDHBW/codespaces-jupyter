
import pyautogui
import math
import time

time.sleep(5)
# Radius 
R = 350

# measuring screen size
(x, y) = pyautogui.size()
# locating center of the screen 
(X, Y) = pyautogui.position(x / 2, y / 2,)

# Repeat the process 10 times
for _ in range(10):
    for i in range(360):
        # setting pace with a modulus 
        if i % 6 == 0:
            pyautogui.moveTo(X + R * math.cos(math.radians(i)), Y + R * math.sin(math.radians(i)), duration=1/(2048*8))