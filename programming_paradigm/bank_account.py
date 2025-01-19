class BankAccount:
  def __init__(self, balance=0):
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount

  def withdraw(self, amount):
    if self.balance >= amount:
      self.balance -= amount
      return True
    else:
      return False

  def show_balance(self):
    print(f"Your balance is: ${self.balance}")