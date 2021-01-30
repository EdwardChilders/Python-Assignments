class BankAccount:
  def __init__(self, int_rate = 0.01, balance = 0):
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

class User:
  def __init__(self, name, email_address):
    self.name = name
    self.email = email_address
    self.account = BankAccount(int_rate=0.02, balance=0)

  def make_deposit(self, amount):
    self.account.deposit(amount)
    return self

  def make_withdrawal(self, amount):
    self.account.withdraw(amount)
    return self

  def transfer_money(self, other_user, amount):
    self.account.withdraw(amount)
    other_user.account.deposit(amount)
    return self


micky = User("Micky Mouse", "micky@python.com")
micky.make_deposit(100).account.display_account_info()

micky.account2 = BankAccount(0.02,700)
micky.account2.yield_interest().display_account_info()
