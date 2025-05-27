import random

random_number = int(random.random() * 100) + 1

not_won = True

print(
    "Errate die richtige Zahl zwischen 1 und 100. Ich sage dir, ob deine Zahl höher oder niedriger ist als die gesuchte Zufallszahl."
)
while not_won:
    try:
        user_input = input("Gebe eine ganze Zahl von 1 - 100 ein: ").lower()
        if user_input == "exit":
            break
        else:
            user_input = int(user_input)
        if user_input == random_number:
            not_won == False
            print("Richtig, du hast gewonnen!")
            break
        else:
            if user_input < random_number:
                print(f"Deine Zahl ist niedriger. Versuche es erneut.")
            if user_input > random_number:
                print(f"Deine Zahl ist höher. Versuche es erneut.")
    except:
        print("Das war keine ganze Zahl. Gebe eine Zahl von 1 - 100 ein.")
