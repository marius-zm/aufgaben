running = True
users_list = []

print(
    "Gib mir deine Zahlen und ich schreibe sie in eine Liste, sortiere diese und zeige dir nützliche Informationen über deine Zahlen. Schreibe 'stop', um das Sammeln der Zahlen zu beenden und die Informationen anzuzeigen."
)

while running:
    user_input = input("Gebe eine beliebige ganze Zahl ein: ").lower()

    if user_input == "stop":
        if len(users_list) == 0:
            print("Deine Liste ist Leer. Ich habe nichts für dich.")
            running == False
            break

        sum = 0
        highest_number = users_list[0]
        lowest_number = users_list[0]

        for i in users_list:
            sum += i
            if i > highest_number:
                highest_number = i
            if i < lowest_number:
                lowest_number = i

        print("Hier die Ergebnisse:")
        print(f"Höchste Zahl: {highest_number}")
        print(f"Niedrigste Zahl: {lowest_number}")
        print(f"Durchschnitt: {round((sum / len(users_list)), 2)}")
        users_list_sorted = sorted(users_list)
        print(f"Sortierte Liste: {users_list_sorted}")

        running = False

    else:
        try:
            user_input = int(user_input)
            users_list.append(user_input)
        except:
            print("Das war keine ganze Zahl. Gebe eine ganze Zahl ein.")
