from datetime import datetime

def stunden_berechnen(startzeit, endzeit):
    # Zeitformat: 'HH:MM'
    format_uhrzeit = '%H:%M'
    
    # Konvertiere die eingegebenen Zeiten in datetime-Objekte
    startzeit_obj = datetime.strptime(startzeit, format_uhrzeit)
    endzeit_obj = datetime.strptime(endzeit, format_uhrzeit)
    
    # Berechne die Differenz zwischen Endzeit und Startzeit
    arbeitszeit = endzeit_obj - startzeit_obj
    
    # Gib die Stunden als Dezimalzahl aus
    stunden = arbeitszeit.total_seconds() / 3600
    
    return stunden

# Nutzereingabe für Startzeit und Endzeit
startzeit_input = input("Gib deine Startzeit ein (Format: HH:MM): ")
endzeit_input = input("Gib deine Endzeit ein (Format: HH:MM): ")

# Berechne die Arbeitsstunden
gearbeitete_stunden = stunden_berechnen(startzeit_input, endzeit_input)

# Gib das Ergebnis aus
print("Du hast heute {} Stunden gearbeitet.".format(gearbeitete_stunden))
