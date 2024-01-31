import os
import time

from utils import *
from idea_manager import *
from clipboard_extractor import *
from push_idea import *

if __name__ == "__main__":
    # idee = idee_ziehen()[:-2]
    # name = idee + ".py"

    # print(idee)
    
    url = 'https://chat.openai.com/auth/login'
    open_browser(url)
    click_at_position(721.0, 842)
    
    # # Ask GPT and Copy the Output
    # perform_login()
    # time.sleep(5)
    # ask_chat_gpt(idee)
    # clickOnCopy()
    # time.sleep(1)
    # pyautogui.hotkey('ctrl', 'w')
    
    
    # # extract and push
    # extract_code_from_clipboard(name)
    # time.sleep(2)
    # create_and_push_commit_file(name,"new Programm")


# 1. Clicks in Prozent (mit Anzahl der Pixel, pyautogui hat ein Befehl für das anzeigen der Anzahl)
# 2. Chat, nach Benutzung löschen
# 3. Nach Copied wechsel zu VSC
# 4. Diskussion über Selenium, xPath
# 5. Programm soll nach 7 Tagen gelöscht werden 