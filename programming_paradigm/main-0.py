from bank_account import BankAccount

my_account = BankAccount(250)  # Starting with $100

while True:
  print("\nChoose an option:")
  print("1. Deposit")
  print("2. Withdraw")
  print("3. Check Balance")
  print("4. Exit")

  choice = input("Enter your choice (1-4): ")

  if choice == '1':
    amount = float(input("Enter deposit amount: "))
    my_account.deposit(amount)
    print(f"Deposited: ${amount}")

  elif choice == '2':
    amount = float(input("Enter withdrawal amount: "))
    if my_account.withdraw(amount):
      print(f"Withdraw: ${amount}")
    else:
      print("Insufficient funds.")

  elif choice == '3':
    my_account.show_balance()

  elif choice == '4':
    print("Goodbye!")
    break

  else:
    print("Invalid choice. Please try again.")