# # # #
# # problem here was to get the right points so it selects the wanted text (the theme of this weeks discussion)
# def copyDiscussion():
#     upRightCorner = pyautogui.locateCenterOnScreen(r'Projekt\buttons\upRightCornerGIT.png')
#     bottomLeftCorner = pyautogui.locateCenterOnScreen(r'Projekt\buttons\bottomLeftCornerGIT.png')    
        
#     if upRightCorner is not None and bottomLeftCorner is not None:
#         pyautogui.moveTo(upRightCorner)
#         pyautogui.dragTo(bottomLeftCorner)
#         print("discussion copied")
#     else:
#         print("failed to copy discussion")
        
        

# # well that was the first try, works only if it's a short discussion
# def copyDiscussion():
#     upRightCorner = pyautogui.locateCenterOnScreen(r'Projekt\buttons\upRightCornerGIT.png')
#     bottomLeftCorner = pyautogui.locateCenterOnScreen(r'Projekt\buttons\bottomLeftCornerGIT.png')    
        
#     if upRightCorner is not None and bottomLeftCorner is not None:
#         pyautogui.moveTo(upRightCorner)
#         pyautogui.mouseDown()  # Press the mouse button
#         pyautogui.moveTo(bottomLeftCorner)
#         pyautogui.mouseUp()  # Release the mouse button
#         print("discussion copied")
#     else:
#         print("failed to copy discussion")


# # didn't work, because one part get's send immediatly, because of newline 
# def editDiscussion(file_path):
#     # Text aus der Zwischenablage kopieren
#     clipboard_text = pyperclip.paste()

#     # Find the index of the last sentence separator
#     last_sentence_index = clipboard_text.rfind('_Originally')

#     # Remove the last sentence if found
#     if last_sentence_index != -1:
#         clipboard_text = clipboard_text[:last_sentence_index].strip()  # Remove leading and trailing whitespace

#     # save edited discussion in new .txt-file
#     with open(file_path, 'w') as file:
#         file.write(clipboard_text)



    
# # ask chat for feedback
# def askChatForComment():
#     editDiscussion(r'Projekt\discussion.txt')
    
#     promtLine = pyautogui.locateCenterOnScreen(r'Projekt\buttons\promtLineChat.png')
    
#     # Read content from discussion.txt
#     with open(r'Projekt\discussion.txt', 'r') as file:
#         description_lines = file.readlines()
#         description = ' '.join(description_lines).strip()  # Concatenate lines without newlines, newlines caused to early 'enter'

#     if promtLine is not None:
#         pyautogui.moveTo(promtLine)
#         x, y = promtLine
#         pyautogui.click(x-200, y)
#         pyautogui.typewrite("Write a short and positive Feedback to the following description: ")
#         pyautogui.typewrite(description)
#         time.sleep(3)
#         pyautogui.hotkey('enter')
#         print("able to ask Chat")
        
#     else:
        print("can't ask Chat")
