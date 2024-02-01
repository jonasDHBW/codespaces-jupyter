import os
import time

from utils import *
from idea_manager import *
from clipboard_extractor import *
from push_idea import *

if __name__ == "__main__":
    # Dimension abrufen
    get_screen_dimensions
    ()
    
    # idee auswählen
    idee = idee_ziehen()[:-2]
    name = idee + ".py"

    print(idee)
    
    url = 'https://chat.openai.com/auth/login'
    open_browser(url)
    click_at_position(721, 842)
    
    # Ask GPT and Copy the Output
    perform_login()
    time.sleep(5)
    ask_chat_gpt(idee)
    clickOnCopy()
    time.sleep(1)
    
    # delete Chat and close Tab
    deleteChat()
    close_browser()
    
    # extract and push
    extract_code_from_clipboard(name)
    time.sleep(2)
    create_and_push_commit_file(name,"new Programm")


# 1. Clicks in Prozent (mit Anzahl der Pixel, pyautogui hat ein Befehl für das anzeigen der Anzahl) -> Check
# 2. Chat, nach Benutzung löschen -> Check
# 3. Nach Copied wechsel zu VSC -> Browser wird geschlossen
# 4. Diskussion über Selenium, xPath
# 5. Programm soll nach 7 Tagen gelöscht werden 