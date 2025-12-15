import art
import random
import game_data

game_data = game_data.data
continue_game = True
# restarts Game
def restart_game():
    print("\n" * 30)
    game_start()
#formats the data for game use
def get_data(option):
    option_name = option["name"]
    option_descr = option["description"]
    option_country = option["country"]
    return f"{option_name}, a {option_descr}, from {option_country}"
# sees if the players answer is correct
def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

def game_start():
    global continue_game
    score = 0
    option_a = random.choice(game_data)
    option_b = random.choice(game_data)
    print(art.logo)
    # this is the actual game
    while continue_game:
        # grabs the follower count from options a and b
        a_followers = option_a["follower_count"]
        b_followers = option_b["follower_count"]
        # changes option a if both options are the same
        if option_a == option_b:
            option_b = random.choice(game_data)

        print(f"{get_data(option_a)}\n {art.vs}\n {get_data(option_b)}")

        player_choice = input("Who has more followers? A or B? ").lower()
        # checks if the players guess was right
        is_right = check_answer(player_choice, a_followers, b_followers)

        if is_right:
            score += 1
            print(f"{art.logo}\n That's right! Your Score: {score}")
        else:
            print(f"{art.logo}\n That's wrong, better luck next time! Final Score: {score}")
            play_again = input("Would you like to play again? Y or N? ").lower()
            if play_again == "y":
                restart_game()
            else:
                continue_game = False
        # moves option b to a and resets option b
        option_a = option_b
        option_b = random.choice(game_data)

game_start()