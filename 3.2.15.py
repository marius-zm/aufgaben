class BankAccount:
    def __init__(self, owner, balance = 0.0, limit = -100) -> None:
        self.owner = owner
        self.balance = balance
        self.limit = limit

    def pay_in(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0.")
            return
        self.balance += amount

    def pay_out(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0.")
            return
        if self.balance - amount < self.limit:
            print("That would exceed your account overdraft limit.")
            return
        self.balance -= amount
        self.show_balance()

    def show_balance(self):
        print(f"{self.balance}")

    def __str__(self) -> str:
        print(f"Kontoinhaber: {self.owner} - Kontostand: {self.balance}")

    def calc_zinsen(self, zinssatz):
        if zinssatz <= 0:
            print("Zinssatz must be higher than 0.")
            return
        if self.balance > 0:
            self.balance += self.balance * (zinssatz / 100)
            print(f"New account balance: {self.balance}")
        else:
            print("Accountbalance not positiv.")

account1 = BankAccount("Marius Meyer")
account1.show_balance()
account1.pay_in(100)
account1.show_balance()
account1.calc_zinsen(10)
account1.pay_out(200)
account1.pay_out(20)
account1.__str__()