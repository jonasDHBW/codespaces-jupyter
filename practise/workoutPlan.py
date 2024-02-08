import random

# Liste von Übungen mit realistischen Mindest- und Höchstwerten für Satzzahlen und Pausenzeit in Sekunden
exercise_list = {
    "Kniebeugen": {},
    "Liegestütze": {},
    "Klimmzüge": {},
    "Crunches": {},
    "Ausfallschritte": {},
    "Burpees": {},
    "Planks": {},
    "Seilspringen": {},
    "Trizepsdips": {},
    "Russian Twists": {},
    "Schulterdrücken": {},
    "Bizepscurls": {},
    "Beinheben": {},
    "Fahrradfahren": {},
    "Rückenstrecker": {}
}

def generate_sets(min_sets, max_sets):
    """
    Generiert eine zufällige Anzahl von Sätzen innerhalb eines bestimmten Bereichs.
    """
    return random.randint(min_sets, max_sets)

def generate_rest_time(min_rest_time, max_rest_time):
    """
    Generiert eine zufällige Pausenzeit innerhalb eines bestimmten Bereichs.
    """
    return random.randint(min_rest_time, max_rest_time)

def generate_training_plan(exercise_list, num_exercises=10):
    """
    Generiert einen zufälligen Trainingsplan mit einer bestimmten Anzahl von Übungen.
    """
    training_plan = random.sample(list(exercise_list.keys()), num_exercises)
    for exercise in training_plan:
        exercise_list[exercise]["Sätze"] = generate_sets(3, 5)  # Annahme: 3-5 Sätze
        exercise_list[exercise]["Pausenzeit"] = generate_rest_time(20, 90)  # Annahme: 20-90 Sekunden
    return training_plan

def main():
    print("Willkommen beim Trainingsplan-Generator!")
    print("Hier ist dein zufälliger Trainingsplan für heute:")

    # Generiere einen Trainingsplan mit 10 Übungen
    training_plan = generate_training_plan(exercise_list)

    # Zeige den Trainingsplan an
    for index, exercise in enumerate(training_plan, start=1):
        print(f"{index}. {exercise}:")
        print(f"   Sätze: {exercise_list[exercise]['Sätze']}")
        print(f"   Pausenzeit: {exercise_list[exercise]['Pausenzeit']} Sekunden\n")

if __name__ == "__main__":
    main()
