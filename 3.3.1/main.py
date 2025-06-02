from classes.BankAccount import BankAccount


account1 = BankAccount("Marius Meyer")
account1.show_balance()
account1.pay_in(100)
account1.show_balance()
account1.calc_interest(10)
account1.pay_out(200)
account1.pay_out(20)
account1.calc_interest(3)
print(account1)
