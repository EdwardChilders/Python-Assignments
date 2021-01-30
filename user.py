class User:
  def __init__(self, name, email_address):# now our method has 2 parameters!
    self.name = name			# and we use the values passed in to set the name attribute
    self.email = email_address		# and the email attribute
    self.account_balance = 0

  def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    self.account_balance += amount	# the specific user's account increases by the amount of the value received

  def make_withdrawal(self, amount):
    self.account_balance -= amount

  def display_user_balance(self):
    print (f"User: {self.name}, Balance: {self.account_balance}")

  def transfer_money(self, other_user, amount):
    self.account_balance -= amount
    other_user.account_balance += amount

guido = User("Guido van Rossum", "guido@python.com")
micky = User("Micky Mouse", "micky@python.com")
monty = User("Monty Python", "monty@python.com")


print(guido.name)	# output: Guido van Rossum
print(micky.name) # output: Micky Mouse
print(monty.name)	# output: Monty Python



guido.make_deposit(100)
guido.make_deposit(500)
guido.make_deposit(777)
guido.make_withdrawal(300)
guido.display_user_balance()

micky.make_deposit(75679)
micky.make_deposit(2673405)
micky.make_withdrawal(777)
micky.make_withdrawal(23456)
micky.display_user_balance()

monty.make_deposit(500)
monty.make_withdrawal(50)
monty.make_withdrawal(250)
monty.make_withdrawal(23)
monty.display_user_balance()

guido.transfer_money(monty, 300)
guido.display_user_balance()
monty.display_user_balance()


# print(guido.account_balance)
# print(monty.account_balance)
# print(micky.account_balance)







