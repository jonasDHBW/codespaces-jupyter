import random

def zahlenraten():
    zielzahl = random.randint(1, 100)
    versuche = 0

    print("Willkommen beim Zahlenraten-Spiel!")
    print("Ich habe eine Zahl zwischen 1 und 100 ausgewählt. Kannst du sie erraten?")

    while True:
        rate = int(input("Dein Tipp: "))
        versuche += 1

        if rate == zielzahl:
            print(f"Glückwunsch! Du hast die Zahl {zielzahl} in {versuche} Versuchen erraten.")
            break
        elif rate < zielzahl:
            print("Zu niedrig. Versuche es erneut.")
        else:
            print("Zu hoch. Versuche es erneut.")

if __name__ == "__main__":
    zahlenraten()
