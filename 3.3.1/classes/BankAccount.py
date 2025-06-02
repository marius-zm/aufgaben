class BankAccount:
    def __init__(self, owner, balance=0.0, limit=-100) -> None:
        self.owner = owner
        self.balance = balance
        self.limit = limit

    def pay_in(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0.")
            return
        self.balance += amount
        print(f"New Account balance: {self.balance}")

    def pay_out(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0.")
            return
        if self.balance - amount < self.limit:
            print("That would exceed your account overdraft limit.")
            return

        self.balance -= amount
        print(f"New Account balance: {self.balance}")

    def show_balance(self):
        print(f"Account balance: {self.balance}")

    def __str__(self) -> str:
        return f"Account owner: {self.owner} - Account balance: {self.balance}"

    def calc_interest(self, interest_rate):
        if interest_rate <= 0:
            print("Interest rate must be higher than 0.")
            return
        if self.balance > 0:
            self.balance += self.balance * (interest_rate / 100)
            print(f"New account balance: {self.balance}")
        else:
            print("Account balance not positive.")