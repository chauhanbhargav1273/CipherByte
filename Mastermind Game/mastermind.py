import random

def provide_feedback(secret, guess):
    correct_position = sum(s == g for s, g in zip(secret, guess))
    correct_digit = sum(min(secret.count(x), guess.count(x)) for x in set(guess))
    return correct_position, correct_digit - correct_position

def mastermind_game():
    def get_secret_code():
        while True:
            code = input("Enter a multi-digit secret number: ")
            if code.isdigit():
                return code
            print("Invalid input. Please enter a valid multi-digit number.")

    def get_guess():
        while True:
            guess = input("Enter your guess: ")
            if guess.isdigit():
                return guess
            print("Invalid input. Please enter a valid multi-digit number.")

    def player_turn(player_number):
        print(f"\nPlayer {player_number}, it's your turn to set the secret number.")
        secret_code = get_secret_code()
        attempts = 0
        while True:
            attempts += 1
            print(f"\nPlayer {3 - player_number}, it's your turn to guess.")
            guess = get_guess()
            if guess == secret_code:
                print(f"Correct! You guessed the number in {attempts} attempts.")
                return attempts
            correct_position, correct_digit = provide_feedback(secret_code, guess)
            print(f"Correct digits in the correct position: {correct_position}")
            print(f"Correct digits in the wrong position: {correct_digit}")

    print("Welcome to the Mastermind Game!")

    # Player 1's turn
    print("\nPlayer 1 will set the secret number first.")
    attempts_player1 = player_turn(1)

    # Player 2's turn
    print("\nNow Player 2 will set the secret number.")
    attempts_player2 = player_turn(2)

    # Determine the winner
    if attempts_player1 < attempts_player2:
        print("\nPlayer 1 wins and is crowned Mastermind!")
    elif attempts_player2 < attempts_player1:
        print("\nPlayer 2 wins and is crowned Mastermind!")
    else:
        print("\nIt's a tie! Both players are Masterminds!")

if __name__ == "__main__":
    mastermind_game()
