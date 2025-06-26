from util.functions import menu

menu()

expenditures = []
income = []


def show_overview():
    print("Expenditures: ", sum(expenditures))
    print("Income: ", sum(income))
    print("Saldo: ", calc_saldo())


def calc_saldo():
    return round(sum(income) - sum(expenditures), 2)


saldo = calc_saldo()

while True:
    choice = input("> ")

    try:
        if choice == "exit":
            break

        choice = int(choice)

    except ValueError as e:
        print("That was no number. Type 1, 2 or 3.", e)

    match choice:
        case 1:
            menu()
        case 2:
            show_overview()
        case 3:
            while True:
                try:
                    expenditure = abs(float(input("How much is the expenditure? ")))
                except ValueError as e:
                    print("That was no number. Type again.", e)
                    continue
                expenditures.append(expenditure)
                print("Current expenditures: ", sum(expenditures))
                saldo = calc_saldo()
                break
        case 4:
            while True:
                try:
                    income_input = abs(float(input("How much is the income? ")))
                except ValueError as e:
                    print("That was no number. Type again.", e)
                    continue
                income.append(income_input)
                print("Current income: ", sum(income))
                saldo = calc_saldo()
                break
        case _:
            print("default")
        
    if (saldo < 0):
        print("Warning: Your current saldo is below 0.")
        print(saldo)
