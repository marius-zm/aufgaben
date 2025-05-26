# if - elif - else - and - or

name_list = ["luigi,", "batman", "peach", "marius"]

age = int(input("Wie alt bist du? "))
name = input("Wie heißt du? ")

if age < 20:
    print("Du bist zu jung für dieses Programm!")
elif name.lower() in name_list:
    print("Ah, du stehst auf der Namensliste, willkommen.")
elif age >= 20 and age <= 30:
    print("Dieses Program ist ü30 oder du stehst auf der Namensliste.") 
elif age == 100:
    print("Wow, der heutige Abend geht für dich auf's Haus!")
elif age > 30:
    print("Willkommen im Klub.")
else:
    print("Du kommst hier net rein!")
