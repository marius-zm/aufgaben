def menu():
    print("MENU")
    print("1 - Show Menu")
    print("2 - Show Overview")
    print("3 - Add expenditure")
    print("4 - Add income")
    print("exit - Exit program")

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    window.geometry(f"{width}x{height}+{int(x)}+{int(y)}")