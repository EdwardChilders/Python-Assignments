class BankAccount:
  def __init__(self, int_rate, balance): # don't forget to add some default values for these parameters!
    self.account_balance = 0
    self.interest = int_rate
    self.account_balance = balance

  def deposit(self, amount):
    self.account_balance += amount
    return self

  def withdraw(self, amount):
    if self.account_balance < amount:
      print("Insufficient funds: Charging a $5 fee")
      self.account_balance -= 5
    else:
      self.account_balance -= amount
    return self

  def display_account_info(self):
    print (f"Balance: {self.account_balance}")
    return self

  def yield_interest(self):
    if self.account_balance > 0:
      self.account_balance += self.account_balance*self.interest
    return self

account1 = BankAccount(0.05, 700)
account2 = BankAccount(0.03, 300)

account1.deposit(150).deposit(50).deposit(75).withdraw(350).yield_interest().display_account_info()
account2.deposit(50).deposit(20).withdraw(30).withdraw(10).withdraw(25).withdraw(90).yield_interest().display_account_info()

#  To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)