class BankAccount:
    def __init__(self, owner) -> None:
        self.owner = owner
        self.balance = 0
        self.limit = 100

    def pay_in(self, amount):
        self.balance += amount

    def pay_out(self, amount):
        if self.balance - self.limit < amount:
            print("Du hast nicht genug Geld auf dem Konto.")
            return
        self.balance -= amount

    def show_balance(self):
        print(f"{self.balance}")

    def __str__(self) -> str:
        print(f"Kontoinhaber: {self.owner} - Kontostand: {self.balance}")

    def calc_zinsen(self, zinssatz):
        if self.balance > 0:
            self.balance += self.balance * zinssatz
