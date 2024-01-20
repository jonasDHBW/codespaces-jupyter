# clipboard_extractor.py
import re
import pyperclip

class ClipboardExtractor:
    @staticmethod
    def extract_code(text):
        # Definieren Sie einen regulären Ausdruck, um Code zu erkennen (z.B. beginnt mit "```" und endet mit "```")
        code_pattern = r'```([\s\S]*?)```'

        # Finden Sie alle Übereinstimmungen des regulären Ausdrucks im Text
        code_matches = re.findall(code_pattern, text)

        # Rückgabe der extrahierten Code-Abschnitte
        return code_matches

    @staticmethod
    def extract_code_from_clipboard():
        # Text aus der Zwischenablage kopieren
        clipboard_text = pyperclip.paste()

        # Extrahieren Sie den Code aus dem kopierten Text
        extracted_code = ClipboardExtractor.extract_code(clipboard_text)

        # Drucken Sie den extrahierten Code
        for code_block in extracted_code:
            print("Extrahierter Code:")
            print(code_block)

if __name__ == "__main__":
    ClipboardExtractor.extract_code_from_clipboard()
