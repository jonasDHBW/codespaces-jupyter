import pyautogui
import time
 
time.sleep(3)

def findBell():
    # Verzögerung vor der Suche nach dem ersten Bild
    time.sleep(2)
    
    # Suche nach dem ersten Bild
    dots_location = pyautogui.locateCenterOnScreen(r'Projekt\buttons\dotsDiscord.png')
    
    # Überprüfen, ob das Bild gefunden wurde
    if dots_location:
        # Bewegen Sie den Mauszeiger zu den Koordinaten und klicken Sie darauf
        pyautogui.moveTo(dots_location)
        pyautogui.click()
        
        # Verzögerung vor der Suche nach dem zweiten Bild
        time.sleep(2)
        
        # Suche nach dem zweiten Bild
        bell_location = pyautogui.locateCenterOnScreen(r'Projekt\buttons\bellDiscord.png')
        
        # Überprüfen, ob das zweite Bild gefunden wurde
        if bell_location:
            # Bewegen Sie den Mauszeiger zu den Koordinaten und klicken Sie darauf
            pyautogui.moveTo(bell_location)
            pyautogui.click()
        else:
            print("Das Bild 'bellDiscord.png' wurde nicht gefunden.")
    else:
        print("Das Bild 'dotsDiscord.png' wurde nicht gefunden.")

    
findBell()