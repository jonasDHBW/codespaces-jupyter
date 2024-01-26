from datetime import datetime

def stunden_berechnen(startzeit, endzeit, pausenzeit):
    # Zeitformat: 'HH:MM'
    format_uhrzeit = '%H:%M'
    
    # Konvertiere die eingegebenen Zeiten in datetime-Objekte
    startzeit_obj = datetime.strptime(startzeit, format_uhrzeit)
    endzeit_obj = datetime.strptime(endzeit, format_uhrzeit)
    
    # Berechne die Differenz zwischen Endzeit und Startzeit
    arbeitszeit = endzeit_obj - startzeit_obj
    
    # Konvertiere die Pausenzeit in datetime-Objekt
    pausenzeit_obj = datetime.strptime(pausenzeit, format_uhrzeit)
    
    # Subtrahiere die Pausenzeit von der Arbeitszeit
    arbeitszeit -= pausenzeit_obj
    
    # Berechne die Stunden als Dezimalzahl
    stunden = arbeitszeit.total_seconds() / 3600
    
    return stunden

# Nutzereingabe für Startzeit, Endzeit und Pausenzeit
startzeit_input = input("Gib deine Startzeit ein (Format: HH:MM): ")
endzeit_input = input("Gib deine Endzeit ein (Format: HH:MM): ")
pausenzeit_input = input("Gib deine Pausenzeit ein (Format: HH:MM): ")

# Berechne die Arbeitsstunden
gearbeitete_stunden = stunden_berechnen(startzeit_input, endzeit_input, pausenzeit_input)

# Gib das Ergebnis aus
print("Du hast heute {} Stunden gearbeitet.".format(gearbeitete_stunden))
