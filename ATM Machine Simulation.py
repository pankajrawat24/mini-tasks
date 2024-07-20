import time

print("Please insert your card.")
# Simulate card processing time
time.sleep(3)


def validate_pin(entered_pin):
    password = 1234  # Store PIN securely (replace with a more secure storage method)
    return entered_pin == password


def change_pin(current_pin):
    attempts = 0
    max_attempts = 3
    while attempts < max_attempts:
        current_pin_entered = int(input("Enter your current PIN: "))
        if validate_pin(current_pin_entered):
            new_pin = int(input("Enter your new PIN: "))
            confirm_pin = int(input("Confirm your new PIN: "))
            if new_pin == confirm_pin:
                print("PIN changed successfully.")
                return new_pin
            else:
                print("PIN confirmation doesn't match. Please try again.")
        else:
            attempts += 1
            if attempts == max_attempts:
                print(f"Incorrect current PIN. Maximum attempts reached. Returning to main menu.")
                return current_pin  # Return current_pin so the user doesn't lose access
            else:
                print(f"Incorrect current PIN. You have {max_attempts - attempts} attempts remaining.")
    return current_pin  # Return current_pin in case of all attempts failing


# Improved pin entry loop with maximum attempts
max_attempts = 3
attempts = 0
while attempts < max_attempts:
    pin = int(input("Enter your ATM PIN: "))
    if validate_pin(pin):
        print("PIN accepted.")
        break
    else:
        attempts += 1
        print(f"Incorrect PIN. You have {max_attempts - attempts} attempts remaining.")

if attempts == max_attempts:
    print("Maximum attempts reached. Card blocked. Please contact your bank.")
    exit()

# User account balance and transaction history
balance = 5000
transactions = []  # List to store transactions


# Main ATM menu loop
while True:
    print("""
    1. Check Balance
    2. Withdraw Cash
    3. Deposit Cash
    4. Change PIN
    5. View Transaction History
    6. Exit
    """)

    try:
        option = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid option. Please enter a number (1-6).")
        continue

    if option == 1:
        print(f"Your current balance is: ${balance}")

    elif option == 2:
        withdraw_amount = int(input("Enter amount to withdraw: "))

        # Check for sufficient funds
        if withdraw_amount > balance:
            print("Insufficient funds. Please enter a lower amount.")
            continue

        # Dispense cash (simulated)
        print(f"Dispensing ${withdraw_amount}...")
        time.sleep(2)  # Simulate cash dispensing time
        balance -= withdraw_amount
        print(f"Withdrawal successful. Your updated balance is: ${balance}")
        transactions.append(f"- Withdrawal: ${withdraw_amount}")

    elif option == 3:
        deposit_amount = int(input("Enter amount to deposit: "))
        balance += deposit_amount
        print(f"Deposit successful. Your updated balance is: ${balance}")
        transactions.append(f"+ Deposit: ${deposit_amount}")

    elif option == 4:
        current_pin = change_pin(validate_pin(int(input("Enter your current PIN to proceed: "))))

    elif option == 5:
        if not transactions:
            print("No transactions found yet.")
        else:
            print("Transaction History:")
            for transaction in transactions:
                print(transaction)

    elif option == 6:
        print("Thank you for using our ATM. Please collect your card.")
        break

    else:
        print("Invalid option. Please enter a number (1-6).")
