import pyautogui
import time

# Standard-Bildschirmauflösung
standard_screen_width, standard_screen_height = 1920, 1080

# Ermitteln Sie die aktuelle Bildschirmauflösung
screen_width, screen_height = pyautogui.size()

# Verhältnis zwischen der aktuellen Auflösung und der Standardauflösung berechnen
width_ratio = screen_width / standard_screen_width
height_ratio = screen_height / standard_screen_height

# Warten Sie für 3 Sekunden, um sicherzustellen, dass der Bildschirm bereit ist
time.sleep(3)

# Suchen Sie nach dem Bild und erhalten Sie die BoundingBox



# Überprüfen, ob das Bild gefunden wurde
if start is not None:
    # Extrahieren Sie die prozentualen x- und y-Werte aus der BoundingBox
    button_percentage_x = (button_x / standard_screen_width) * 100
    button_percentage_y = (button_y / standard_screen_height) * 100

    # Berechnen Sie die tatsächlichen Bildschirmkoordinaten des Buttons unter Berücksichtigung des Verhältnisses
    button_x_actual = int((button_percentage_x / 100) * screen_width)
    button_y_actual = int((button_percentage_y / 100) * screen_height)

    # Klicken Sie auf den Button
    pyautogui.click(button_x_actual, button_y_actual)

    print(f"Tatsächliche X-Wert: {button_x_actual}, Tatsächliche Y-Wert: {button_y_actual}")
else:
    print("Bild nicht gefunden.")
