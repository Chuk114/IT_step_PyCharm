class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"На рахунок {self.account_number} зараховано {amount} грн.")
        else:
            print("Сума поповнення повинна бути більшою за 0.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостатньо коштів на рахунку.")
        elif amount <= 0:
            print("Сума зняття повинна бути більшою за 0.")
        else:
            self.balance -= amount
            print(f"З рахунку {self.account_number} знято {amount} грн.")

    def get_balance(self):
        return self.balance
