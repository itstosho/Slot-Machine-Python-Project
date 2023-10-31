MAX_LINES = 3  # Max number of lines in the file
MAX_BET = 100  # Max bet per line
MIN_BET = 1  # Min bet per line

def deposit():
    while True:
        amount = input("Enter amount to deposit: £")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount  # Return the valid amount
            else:
                print("Please enter a number over 0.")
        else:
            print("Please enter a number.")

def get_number_of_lines():
    while True:
        lines = input(f"Enter number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:  # Check the number is between 1 and MAX_LINES
                return lines  # Return the valid number of lines
            else:
                print("Please enter a valid number of lines.")
        else:
            print("Please enter a number.")

def get_bet():
    while True:
        amount = input(f"Enter amount to bet (£{MIN_BET}-£{MAX_BET}): £")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount
            else:
                print(f"Amount must be between £{MIN_BET} and £{MAX_BET}.")
        else:
            print("Please enter a number.")

def main():
    balance = deposit()  # Assign the returned value to a variable
    lines = get_number_of_lines()  # Assign the returned value to a variable
    bet = get_bet()  # Assign the returned value to a variable
    total_bet = bet * lines  # Calculate the total bet
    print("Balance:", balance)
    print("Lines:", lines)
    print(f"You are betting £{bet} on {lines} lines. Total bet: £{total_bet}")

if __name__ == "__main__":
    main()

