import random

random_number = int(random.random() * 100) + 1

running = True
users_list = []

print(
    "Gib mir deine Zahlen und ich mache etwas."
)

while running:
    user_input = input("Gebe eine beliebige ganze Zahl ein: ").lower()

    if user_input == "stop":
        sum = 0
        highest_number = users_list[0]
        lowest_number = users_list[0]

        for i in users_list:
            sum += i
            if (i > highest_number):
                highest_number = i
            if i < lowest_number:
                lowest_number = i
            
        print("Hier die Ergebnisse:")
        print(f"Höchste Zahl: {highest_number}")
        print(f"Niedrigste Zahl: {lowest_number}")
        print(f"Durchschnitt: {round((sum / len(users_list)), 2)}")
        users_list.sort()
        print(f"Sortierte Liste: {users_list}")

        running = False

    else:
        try:
            user_input = int(user_input)
            users_list.append(user_input)
        except:
            print("Das war keine ganze Zahl. Gebe eine Zahl von 1 - 100 ein.")

    

    # if user_input == random_number:
    #     not_won == False
    #     print(f"Richtig, du hast gewonnen! Du brauchtest dafür {guesses} Versuche.")
    #     break

    # else:
    #     if user_input > 100 or user_input < 1:
    #         print("Die Zahl muss zwischen 1 und 100 liegen.")
    #         continue
    #     if user_input < random_number:
    #         print(f"Deine Zahl ist niedriger. Versuche es erneut.")
    #     if user_input > random_number:
    #         print(f"Deine Zahl ist höher. Versuche es erneut.")
