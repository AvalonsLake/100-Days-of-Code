import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

get_player_choice = int(input("Lets play! what do you choose? Type 0 for Rock, type 1 for Paper, type 2 for Scissors: \n"))

get_comp_choice = random.randint(0, len(options) - 1)

player_choice = options[get_player_choice]
comp_choice = options[get_comp_choice]

print(f"You chose\n {player_choice}\n   \n Computer chose\n {comp_choice}")

# Win Conditions
if player_choice == scissors and comp_choice == paper or player_choice == paper and comp_choice == rock or player_choice == rock and comp_choice == scissors:
    print("You win!")
# Lose conditions
elif player_choice == scissors and comp_choice == rock or player_choice == rock and comp_choice == paper or player_choice == paper and comp_choice == scissors:
    print("You lose!")
# Tie
elif player_choice == comp_choice:
    print("It's a tie!")
