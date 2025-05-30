import random

random_number = int(random.random() * 100) + 1

not_won = True
guesses = 0

print(
    "Errate die richtige Zahl zwischen 1 und 100. Ich sage dir, ob deine Zahl höher oder niedriger ist als die gesuchte Zufallszahl. Schreibe 'exit', um das Spiel zu beenden."
)

while not_won:
    try:
        user_input = input("Gebe eine ganze Zahl von 1 - 100 ein: ").lower()
        guesses += 1

        if user_input == "exit":
            break
        else:
            user_input = int(user_input)

    except:
        print("Das war keine ganze Zahl. Gebe eine Zahl von 1 - 100 ein.")

    if user_input == random_number:
        not_won == False
        print(f"Richtig, du hast gewonnen! Du brauchtest dafür {guesses} Versuche.")
        break

    else:
        if user_input > 100 or user_input < 1:
            print("Die Zahl muss zwischen 1 und 100 liegen.")
            continue
        if user_input < random_number:
            print(f"Deine Zahl ist niedriger. Versuche es erneut.")
        if user_input > random_number:
            print(f"Deine Zahl ist höher. Versuche es erneut.")
