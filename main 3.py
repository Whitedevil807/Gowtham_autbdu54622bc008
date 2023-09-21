class BankAccount:

  def __init__(self, account_number, account_holder_name, initial_balance):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      print(f"Deposited ${amount}. New balance is ${self.__account_balance}")
    else:
      print("Invalid deposit amount. Amount must be greater than zero.")

  def withdraw(self, amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
      print(f"Withdrew ${amount}. New balance is ${self.__account_balance}")
    elif amount > self.__account_balance:
      print("Insufficient funds.")
    else:
      print("Invalid withdrawal amount. Amount must be greater than zero.")

  def display_balance(self):
    print(
        f"Account balance for {self.__account_holder_name}: ${self.__account_balance}"
    )


# Creating an instance of the BankAccount class
account = BankAccount("123456", "John Doe", 1000.00)

# Testing deposit and withdrawal functionality
account.display_balance()
account.deposit(500.00)
account.withdraw(200.00)
account.display_balance()
