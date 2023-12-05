import random

MAX_LINES = 3
MAX_BET = 100

COLS = 3
ROWS = 3

symbols_amount = {
    "A": 3,
    "B": 4,
    "C": 5,
    "D": 6
}

symbols_values = {
    "A": 4,
    "B": 3,
    "C": 2,
    "D": 1
}


def deposit():
    while True:
        balance = input("How much do you want to deposit $")
        if balance.isdigit():
            if 1 <= int(balance) <= 100:
                return int(balance)
            else:
                print("Please, type a number in range 1 - 100!")
        else:
            print("Please, type a number in range 1 - 100!")


def get_bet(balance):
    while True:
        lines_number = input("How much lines do you want to bet on: ")
        if lines_number.isdigit():
            if 1 <= int(lines_number) <= MAX_LINES:
                break
            else:
                print(f"Type a number in range 1 - {MAX_LINES} ")
        else:
            print(f"Type a number in range 1 - {MAX_LINES} ")

    while True:
        bet = input("How much do you want to bet $")
        if bet.isdigit():
            if 0 <= int(bet) and int(lines_number) * int(bet) <= int(balance):
                break
            else:
                print(f"Please enter a number in range 0 - {int(balance) // int(lines_number)}")
        else:
            print(f"Please enter a number in range 0 - {int(balance) // int(lines_number)}")

    return int(bet), int(lines_number)


def spin(symbols_amount):
    symbols = []
    for symbol, amount in symbols_amount.items():
        for i in range(amount):
            symbols.append(symbol)

    cur_spin = []
    random.shuffle(symbols)
    for _ in range(COLS):
        cur_col = []
        cur_symbols = symbols[:]
        for _ in range(ROWS):
            random_choice = random.choice(cur_symbols)
            cur_col.append(random_choice)
            cur_symbols.remove(random_choice)

        cur_spin.append(cur_col)

    return cur_spin


def print_spin(spin):
    for row in range(len(spin[0])):
        for i, col in enumerate(spin):
            if i != len(spin) - 1:
                print(f"{col[row]}", end=" | ")
            else:
                print(f"{col[row]}")


def vinnings(spin, bet, lines, symbols_values):
    cur_win = 0
    bet = int(bet)
    for row in range(int(lines)):
        for index in range(len(spin) - 1):
            try:
                if spin[index][row] != spin[index + 1][row]:
                    break
            except IndexError:
                cur_win += bet * symbols_values[spin[index][row]]
        else:
            cur_win += bet * symbols_values[spin[0][row]]

    return cur_win


def main():
    balance = deposit()

    while True:
        bet, lines = get_bet(balance)
        print(f"You are betting ${bet * lines} on {lines} lines")
        cur_spin = spin(symbols_amount)
        print_spin(cur_spin)
        cur_win = vinnings(cur_spin, bet, lines, symbols_values)
        print(cur_win)
        print(f"You won ${cur_win}")
        balance = balance - bet * lines + cur_win
        if balance > 0:
            print(f"Yor balance is: ${balance}")
        else:
            print("No money in deposit")
            break

        again = input("Press enter to play again or type anything to exit")

        if again != "":
            break

    print(f"You ended your game with ${balance}")


while True:
    main()
    x = input("Press enter to play a new game")
    if x != "":
        break

