def sayHello(name):
    print(f"Hey, {name}, herzlich willkommen.")
    return f"Hey, {name}, herzlich willkommen."

sayHello("marius")

welcome_text = sayHello("birne")

for char in welcome_text:
    print(char)