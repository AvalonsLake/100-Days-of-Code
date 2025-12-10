import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

comp_hand = []
player_hand = []
comp_score = 0
game_over = False

def get_score(player):
    score = 0
    if player:
        for item in player_hand:
            score += item
    else:
        for item in comp_hand:
            score += item
    return score

def deal_cards():
    for number in range(2):
        player_hand.append(cards[random.randint(0, len(cards) - 1)])
        comp_hand.append(cards[random.randint(0, len(cards) - 1)])
    print(f"Your hand is: {player_hand}, current score: {get_score(True)}\n"
          f"Dealers first card: {comp_hand[0]}")

def add_card():
    player_hand.append(cards[random.randint(0, len(cards) - 1)])
    print(f"Your hand: {player_hand}, current score: = {get_score(True)}")

def game_start():
    print(art.logo)
    deal_cards()

    while not game_over:
        if get_score(True) > 21:
            print(f"Final Hand: {player_hand}, current score: {get_score(True)}")
        hit_or_pass = input("Type y to draw another card, type 'n' to pass:").lower()
        if hit_or_pass == 'y':
            add_card()
        else:
            print("idk man")

want_to_play = input("Do you want to play the game? (Y/N): ").lower()
if want_to_play == "y":
    game_start()

