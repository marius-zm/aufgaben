# zimmer = {}

# zimmer['Name'] = str(input("Name des Zimmers: "))
# zimmer['Größe_qm'] = float(input("Größe des Zimmers in qm: "))
# zimmer['Anzahl_Fenster'] = int(input("Wie viele Fenster?: "))
# zimmer['Bodenbelag'] = str(input("Welchen Bodenbelag hat das Zimmer? (Parkett, Teppich?): "))
# zimmer['Wandfarbe'] = str(input("Welche Farbe hat das Zimmer?: "))
# zimmer['Möbliert'] = str(input("Ist das Zimmer möbliert? (j, n): "))
# zimmer['Personen'] = int(input("Wie viele Personen leben in dem Zimmer?: "))
# zimmer['Anzahl_Steckdosen'] = int(input("Wie viele Steckdosen hat das Zimmer?: "))
# zimmer['Balkon'] = str(input("Hat das Zimmer einen Balkon? (j, n): "))
# zimmer['Ventilator'] = str(input("Hat das Zimmer einen Ventilator? (j, n): "))

# print(zimmer)

input_text = [
    "Name: ",
    "Größe in qm: ",
    "Anzahl Fenster: ",
    "Bodenbelag: ",
    "Wandfarbe: ",
    "Möbliert: ",
    "Personen: ",
    "Anzahl Steckdosen: ",
    "Balkon: ",
    "Ventilator: ",
]

user_antworten = []

print("Trage die Werte für ein Zimmer ein, die das Zimmer beschreiben.")

for frage in input_text:
    antwort = str(input(f"{frage}"))
    user_antworten.append(antwort)

print(user_antworten)