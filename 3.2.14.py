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

    def sub_class(self):
        print(f"Ich bin {self.name} und {self.role}.")

marius = Role("Marius", "male", 1.80, "Priester")
marius.greet()
marius.sub_class()