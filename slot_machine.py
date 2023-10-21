import random
import numpy as np

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# Define the count and value for each symbol (A, B, C, D)
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

# Function to check for winning lines
def check_winnings(columns, lines, bet, values):
    # Convert the columns to a NumPy array
    columns = np.array(columns)
    first_row = columns[0]

    # Check for winning lines using NumPy's array comparison
    winning_lines = np.all(columns == first_row, axis=0)
    winning_line_numbers = np.where(winning_lines)[0] + 1

    if winning_line_numbers.size > 0:
        winnings = 0
        for symbol in set(first_row[winning_lines]):
            winnings += bet * values[symbol]
    else:
        winnings = 0

    return winnings, winning_line_numbers

# Function to generate a random spin for the slot machine
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            # Randomly select symbols for each position
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

# Function to print the slot machine output
def print_slot_machine(columns):
    # Transpose the columns for a more intuitive display
    print(np.array(columns).T)

# Function for the player to deposit an initial balance
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

# Function to get the number of lines the player wants to bet on
def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines

# Function to get the bet amount from the player
def get_bet():
    while True:
        amount = input(f"What would you like to bet on each line (between ${MIN_BET} and ${MAX_BET}): $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount

# Function to simulate the player's spin
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    
    if winnings > 0:
        print(f"Congratulations! You won ${winnings}.")
        print(f"You won on lines:", *winning_lines)
    else:
        print("Sorry, you didn't win this time.")

    return winnings - total_bet

# Main game loop
def main():
    print("Welcome to the Slot Machine Game!")
    
    # Get the initial balance from the player
    balance = deposit()
    
    while balance > 0:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play or 'q' to quit: ")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"Thank you for playing! You left with ${balance}")

if __name__ == "__main__":
    main()


