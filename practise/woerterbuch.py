class Woerterbuch:
    def __init__(self):
        self.woerterbuch = {}

    def wort_hinzufuegen(self, wort, bedeutung):
        self.woerterbuch[wort] = bedeutung
        print(f"{wort} wurde dem Wörterbuch hinzugefügt.")

    def wort_suchen(self, wort):
        if wort in self.woerterbuch:
            print(f"{wort}: {self.woerterbuch[wort]}")
        else:
            print(f"{wort} wurde nicht im Wörterbuch gefunden.")

    def alle_woerter_anzeigen(self):
        if not self.woerterbuch:
            print("Das Wörterbuch ist leer.")
        else:
            print("Wörterbuch:")
            for wort, bedeutung in self.woerterbuch.items():
                print(f"{wort}: {bedeutung}")

if __name__ == "__main__":
    woerterbuch_app = Woerterbuch()

    while True:
        print("\nWörterbuch-Anwendung")
        print("1. Wort hinzufügen")
        print("2. Wort suchen")
        print("3. Alle Wörter anzeigen")
        print("4. Beenden")

        auswahl = input("Bitte wählen Sie eine Option (1-4): ")

        if auswahl == "1":
            wort = input("Geben Sie das Wort ein: ")
            bedeutung = input(f"Geben Sie die Bedeutung von {wort} ein: ")
            woerterbuch_app.wort_hinzufuegen(wort, bedeutung)
        elif auswahl == "2":
            wort = input("Geben Sie das zu suchende Wort ein: ")
            woerterbuch_app.wort_suchen(wort)
        elif auswahl == "3":
            woerterbuch_app.alle_woerter_anzeigen()
        elif auswahl == "4":
            print("Das Programm wird beendet. Auf Wiedersehen!")
            break
        else:
            print("Ungültige Eingabe. Bitte wählen Sie eine Option von 1 bis 4.")
