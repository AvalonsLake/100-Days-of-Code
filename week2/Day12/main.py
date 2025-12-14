import random
import art

guesses = 0
game_over = False

def reset_game():
    print("\n" * 30)
    start_game()

def play_again():
    will_play = input("Would you like to play again? Y/N ").lower()
    if will_play == "yes":
        reset_game()
    else:
        return

def start_game():
    global guesses, game_over
    number = random.randint(1, 101)
    print(f"{art.logo}\n"
          f"Welcome to Guess That Number!\n")
    difficulty = input("Would you like to play? Easy or hard? \n").lower()
    if difficulty == "easy":
        guesses = 10
        print("Guess a number between 0 and 100")
    elif difficulty == "hard":
        guesses = 5
        print("Guess a number between 0 and 100")
    else:
        reset_game()

    while not game_over:
        print(f"You have {guesses} guesses left!")
        if guesses == 0:
            print("you lose!")
            play_again()
        player_guess = int(input("Guess a number: "))
        if player_guess == number:
            print(f"{player_guess} is correct! You Won!!")
            game_over = True
        elif player_guess != number:
            if player_guess > number:
                print("Too high!")
            else:
                print("Too low!")
        guesses -= 1

    play_again()

start_game()