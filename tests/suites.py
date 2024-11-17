import unittest
from test_bank_account import BankAccountTest

def bank_account_suite():
  suite = unittest.TestSuite()
  suite.addTest(BankAccountTest("test_deposit_positive"))
  suite.addTest(BankAccountTest("test_withdraw_positive"))
  return suite
  
if __name__ == "__main__":
  runner = unittest.TextTestRunner()
  runner.run(bank_account_suite())