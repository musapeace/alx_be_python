from bank_account import BankAccount

account = BankAccount(250)

while True:
  print("\nChoose an option:")
  print("1. Deposit")
  print("2. Withdraw")
  print("3. Check Balance")
  print("4. Exit")

  choice = input("Enter your choice (1-4): ")

  if choice == '1':
    amount = float(input("Enter deposit amount: "))
    account.deposit(amount)
    print(f"Deposited: ${amount}")

  elif choice == '2':
    amount = float(input("Enter withdrawal amount: "))
    if account.withdraw(amount):
      print(f"Withdraw: ${amount}")
    else:
      print("Insufficient funds.")

  elif choice == '3':
    account.account_balance()

  elif choice == '4':
    print("Goodbye!")
    break

  else:
    print("Invalid choice. Please try again.")