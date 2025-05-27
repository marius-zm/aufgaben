# Einsteiger
def even_or_odd():
    print("Gerade oder ungerade. Das ist hier die Frage.")
    try:
        user_input = int(input("Gib eine Zahl ein: "))
    except:
        print("Das war keine Zahl, gebe eine Zahl ein.")

    if user_input % 2 == 0:
        print("Die Zahl ist gerade.")
    else:
        print("Die zahl ist ungerade.")


even_or_odd()


def pos_or_neg():
    print("Positiv oder negativ oder 0.")

    try:
        user_input = int(input("Gib eine Zahl ein: "))
    except:
        print("Das war keine Zahl. Gib eine Zahl ein.")

    if user_input > 0:
        print(f"Die Zahl {user_input} ist positiv.")
    elif user_input < 0:
        print(f"Die Zahl {user_input} ist negativ.")
    else:
        print(f"Die Zahl ist {user_input}.")


pos_or_neg()


def check_password():
    user_input = input("Hey, hey, hey, gib das geheime Passwort ein: ")
    if user_input == "geheim":
        print("Das Passwort ist korrekt.")
    else:
        print(f"Das Passwort {user_input} ist falsch.")


check_password()


def return_grades():
    noten = [
        "sehr gut",
        "gut",
        "befriedigend",
        "mittlemäßig",
        "schlecht",
        "ungenügend",
    ]

    try:
        user_input = int(input("Gib eine Zahl zwischen 1 und 6 ein: ")) - 1
        if user_input > 6 or user_input < 1:
            print("Die Zahl muss zwischen 1 und 6 sein.")
            return
        print(noten[user_input])
    except:
        print("Das war keine Zahl. Gib eine Zahl ein.")


return_grades()


# Fortgeschrittene


def highest_number():
    print("Gebe mir drei Zahlen und ich werde dir die höchste Zahl zurückgeben.")

    try:
        number_one = int(input("Gib die erste Zahl ein: "))
        number_two = int(input("Gib die zweite Zahl ein: "))
        number_three = int(input("Gib die dritte Zahl ein: "))

        highest_number = number_one

        if number_two > number_one:
            highest_number = number_two
        if number_three > highest_number:
            highest_number = number_three
            print(f"Die höchste Zahl ist: {highest_number}")
        else:
            print(f"Die höchste Zahl ist: {highest_number}")

    except:
        print("Das war keine Zahl. Gib eine Zahl ein.")


highest_number()


def switch_year():
    try:
        user_input = int(input("Gib ein Jahr ein: "))
    except:
        print("Das war keine Zahl. Gib eine Zahl ein.")

    if user_input % 4 == 0 and user_input % 100 != 0 or user_input % 400 == 0:
        print(f"Die Jahreszahl {user_input} ist ein Schaltjahr.")
    else:
        print(f"Die Jahreszahl {user_input} ist KEIN Schaltjahr.")
    # Regel: durch 4 teilbar, aber nicht durch 100, außer es ist durch 400 teilbar)


def number_between():
    print(
        "Gebe mir drei Zahlen und ich sage dir, ob die erste zwischen den anderen zwei Zahlen liegt."
    )

    try:
        number_one = int(input("Gib die erste Zahl ein: "))
        number_two = int(input("Gib die zweite Zahl ein: "))
        number_three = int(input("Gib die dritte Zahl ein: "))

        if (
            number_three < number_one < number_two
            or number_two < number_one < number_three
        ):
            print(
                f"Die erste Zahl {number_one} liegt zwischen {number_two} und {number_three}."
            )
        else:
            print(
                f"Die erste Zahl {number_one} liegt nicht zwischen {number_two} und {number_three}."
            )

    except:
        print("Das war keine Zahl. Gib eine Zahl ein.")


number_between()


def discount():
    print("Ab einem bestimmten Einkaufswert gibt es einen Rabatt.")

    try:
        user_input = float(input("Gib deinen Einkaufswert ein: "))

    except:
        print("Das war keine Zahl. Gib eine Zahl ein.")

    if user_input > 100:
        user_input *= 0.9
        print(f"Neuer Preis: {user_input}")
    else:
        print(f"Rabatt erst ab 100€ Einkaufswert. Kein Rabatt für dich.")


discount()


# Herausfordernd


def traffic_light():
    user_input = input(
        "Gib eine der drei Farben ein (grün, gelb oder rot): "
    ).lower()

    if user_input == "grün":
        print("Es ist grün: fahren")
    elif user_input == "gelb":
        print("Es ist gelb: bereit machen.")
    elif user_input == "rot":
        print("Es ist rot: STOP!")
    else:
        print("Du hast das falsche eingegeben. Gib 'grün', 'gelb' oder 'rot' ein.")


traffic_light()


def bmi_count():
    try:
        user_weight = float(input("Gib dein Gewicht in KG ein: "))
        user_height = float(input("Gib deine Körpergröße in Metern ein: "))
    except:
        print("Das war keine Zahl. Gib eine Zahl ein.")

    bmi_index = user_weight / (user_height * user_height)

    if bmi_index < 18.5:
        print(f"Dein BMI-Index lautet: {bmi_index}, also bist du untergewichtig.")
    elif bmi_index >= 18.5 and bmi_index <= 24.9:
        print(f"Dein BMI-Index lautet: {bmi_index}, also bist du normalgewichtig.")
    else:
        print(f"Dein BMI-Index lautet: {bmi_index}, also bist du übergewichtig.")


# bmi berechnen: gewicht / größe * größe
# Untergewicht: BMI unter 18,5
# Normalgewicht: BMI von 18,5 bis 24,9
# Übergewicht: BMI von 25,0 bis 29,9


bmi_count()


def multiple_choice():
    correct_answer = "A"

    print("Hier die Frage: x")
    print("Antwort A: A")
    print("Antwort B: B")
    print("Antwort C: C")
    print("Antwort D: D")

    user_answer = input(
        "Wie lautet deine Antwort? (Antworte mit A, B, C oder D) "
    ).upper()

    if user_answer == correct_answer:
        print("Deine Antwort ist richtig!")
    else:
        print("Deine Antwort ist falsch.")


multiple_choice()
