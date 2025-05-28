class Person:
    def __init__(self, name, gender, height):
        self.name = name
        self.gender = gender
        self.height = height

    def greet(self):
        print(f"Hey, I'm {self.name}") 

class Role (Person):
    def __init__(self, name, gender, height, role):
        super().__init__(name, gender, height)
    
        self.role = role
        
        if self.role == "Priester":
            self.attributes = {
                "health": 80,
                "armour": 20,
                "intelligence": 15,
                "wisdom": 18,
                "strength": 9,
                "dexterity": 12,
            }

    def sub_class(self):
        print(f"Ich bin {self.name} und {self.role}.")

    def what_are_my_stats(self):
        print(self.attributes)

marius = Role("Marius", "male", 1.80, "Priester")
marius.greet()
marius.sub_class()
marius.what_are_my_stats()