import unittest, os
from src.bank_account import BankAccount

class BankAccountTest(unittest.TestCase):

    def setUp(self) -> None:
        #funcion que se ejecuta antes de cada prueba
        self.account = BankAccount(balance=1000, log_file='transaction_log.txt')

    def tearDown(self):
        #funcion que se ejecuta despues de cada prueba 
        if os.path.exists('transaction_log.txt'):
            os.remove(self.account.log_file)

    def _count_lines(self, filename):
        with open(filename, 'r') as file:
            return len(file.readlines())

    def test_get_balance(self):
        assert self.account.getBalance() == 1000

    def test_deposit_positive(self):
        self.account.deposit(500)
        assert self.account.getBalance() == 1500

    def test_deposit_negative(self):
        self.assertRaises(ValueError,self.account.deposit,-500)

    def test_withdraw_positive(self):
        self.account.withdraw(100)
        assert self.account.getBalance() == 900

    def test_withdraw_negative(self):
        self.assertRaises(ValueError,self.account.withdraw,50000)

    def test_transaction(self):
        assert os.path.exists('transaction_log.txt')
        
    def test_count_transactions(self):
        assert self._count_lines(self.account.log_file) == 1
        self.account.deposit(100)
        assert self._count_lines(self.account.log_file) == 3