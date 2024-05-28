from unittest.mock import patch
import unittest


class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def __str__(self):
        return f"Account {self.account_number}: Balance ${self.balance:.2f}"


class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest_amount = self.balance * (self.interest_rate / 100)
        self.balance += interest_amount


class CurrentAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def send_overdraft_letter(self):
        if self.balance < (self.overdraft_limit * -1):
            print(f"Overdraft letter sent for Account {self.account_number}")


class Bank:
    def __init__(self):
        self.accounts = {}

    def open_account(self, account):
        self.accounts[account.account_number] = account

    def close_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]

    def pay_dividend(self, dividend_amount):
        for account in self.accounts.values():
            account.deposit(dividend_amount)

    def update_accounts(self):
        for account in self.accounts.values():
            if isinstance(account, SavingsAccount):
                account.add_interest()
            elif isinstance(account, CurrentAccount):
                account.send_overdraft_letter()

    def show_accounts(self):
        for account in self.accounts.values():
            print(account)


class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()

    def test_open_acc(self):
        savings = SavingsAccount(account_number=200, balance=100, interest_rate=10)
        current = CurrentAccount(account_number=500, balance=100, overdraft_limit=100)
        self.bank.open_account(savings)
        self.bank.open_account(current)
        self.assertIn(savings.account_number, self.bank.accounts)
        self.assertEqual(self.bank.accounts[savings.account_number].balance, 100)
        self.assertIn(current.account_number, self.bank.accounts)
        self.assertEqual(self.bank.accounts[current.account_number].balance, 100)

    @patch("builtins.print")
    def test_update_acc(self, print_mock):
        savings = SavingsAccount(account_number=200, balance=100, interest_rate=10)
        current = CurrentAccount(account_number=500, balance=-50, overdraft_limit=100)
        self.bank.open_account(savings)
        self.bank.open_account(current)
        self.bank.update_accounts()
        self.assertEqual(self.bank.accounts[savings.account_number].balance, 110)
        print_mock.assert_called_once_with("Overdraft letter sent for Account 500")


if __name__ == '__main__':
    unittest.main()
