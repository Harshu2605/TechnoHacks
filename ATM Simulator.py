accounts = {
    '1234567890': {
        'name': 'John Doe',
        'balance': 1000,
        'pin': '1234'
    },
    '9876543210': {
        'name': 'Jane Smith',
        'balance': 1500,
        'pin': '5678'
    }
}
def display_menu():
    print("ATM Simulator Menu:")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Quit")
def check_balance(account):
    print(f"Account Balance: ${account['balance']}")
def withdraw_money(account, amount):
    if amount > 0 and amount <= account['balance']:
        account['balance'] -= amount
        print(f"Withdrew ${amount}. New balance: ${account['balance']}")
    else:
        print("Invalid amount or insufficient balance.")
def deposit_money(account, amount):
    if amount > 0:
        account['balance'] += amount
        print(f"Deposited ${amount}. New balance: ${account['balance']}")
    else:
        print("Invalid amount.")
while True:
    print("\nWelcome to the ATM Simulator")
    account_number = input("Enter your account number: ")
    if account_number in accounts:
        pin = input("Enter your PIN: ")
        if pin == accounts[account_number]['pin']:
            print(f"Welcome, {accounts[account_number]['name']}!")
            while True:
                display_menu()
                choice = input("Enter your choice (1/2/3/4): ")
                if choice == '1':
                    check_balance(accounts[account_number])
                elif choice == '2':
                    amount = float(input("Enter the amount to withdraw: $"))
                    withdraw_money(accounts[account_number], amount)
                elif choice == '3':
                    amount = float(input("Enter the amount to deposit: $"))
                    deposit_money(accounts[account_number], amount)
                elif choice == '4':
                    print("Thank you for using the ATM Simulator. Have a great day!")
                    break
                else:
                    print("Invalid choice. Please select a valid option (1/2/3/4).")
        else:
            print("Incorrect PIN. Please try again.")
    else:
        print("Account not found. Please check your account number.")
    another_transaction = input("Would you like to perform another transaction? (yes/no): ")
    if another_transaction.lower() != 'yes':
        print("Thank you for using the ATM Simulator. Have a great day!")
        break
