class BankAccount:
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

    def show_info(self):
        print("Власник:", self.name)
        print("Рахунок №:", self.number)
        print("Баланс:", self.balance, "грн.")


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.number] = account

    def transfer(self, from_number, to_number, amount):
        from_acc = self.accounts.get(from_number)
        to_acc = self.accounts.get(to_number)

        if from_acc and to_acc:
            if from_acc.balance >= amount:
                from_acc.withdraw(amount)
                to_acc.deposit(amount)
                print("Переказ виконано.")
            else:
                print("Недостатньо коштів для переказу.")
        else:
            print("Рахунок не знайдено.")


acc1 = BankAccount("Іван", "111", 500)
acc2 = BankAccount("Олена", "222", 300)

bank = Bank()
bank.add_account(acc1)
bank.add_account(acc2)

acc1.deposit(100)
acc2.withdraw(50)
bank.transfer("111", "222", 200)

acc1.show_info()
acc2.show_info()
