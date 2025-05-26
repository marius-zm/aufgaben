# if - elif - else - and - or

name_list = ["luigi,", "batman", "peach", "marius"]

age = int(input("Wie alt bist du? "))
name = input("Wie heißt du? ")

if age > 30 or name.lower() in name_list:
    print("Willkommen im Klub!")
    if age == 100:
        print("Wow, der heutige Abend geht für dich auf's Haus!")
elif age >= 20 and age <= 30:
    print("Dieses Program ist ü30 oder du stehst auf der Namensliste.") 
else:
    print("Du kommst hier net rein!")
