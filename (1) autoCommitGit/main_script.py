# main_script.py
# from utils import initialize_driver, navigate_to_url, click_element
from utils import open_browser, perform_login, ask_chat_gpt
from extract_answer import open_def_tool, open_search_bar, search_for_button
from idea_manager import IdeaManager

if __name__ == "__main__":
    # Benutzerdefinierter Dateipfad für IdeaManager
    custom_file_path = r"C:\Users\jpl\VS Code for Git\codespaces-jupyter\(1) autoCommitGit\ideas.txt"
    
    url = 'https://chat.openai.com/auth/login'
    open_browser(url)

    # Erstelle eine Instanz von IdeaManager mit benutzerdefiniertem Dateipfad
    im = IdeaManager(file_path=custom_file_path)

    perform_login()
    ask_chat_gpt(im)
    open_def_tool()
    open_search_bar()
    search_for_button()


# open ai in python 