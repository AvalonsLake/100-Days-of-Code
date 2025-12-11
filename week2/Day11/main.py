import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

comp_hand = []
player_hand = []

game_over = False

def play():
    player_hand.clear()
    comp_hand.clear()
    want_to_play = input("Do you want to play the game? (Y/N): ").lower()
    if want_to_play == "y":
        game_start()
    else:
        return

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
    print(f"Your hand: {player_hand}, current score: = {get_score(True)}\n"
          f"Dealers first card: {comp_hand[0]}")

def game_start():
    print(art.logo)
    deal_cards()

    while not game_over:
        get_score(True)
        if get_score(True) > 21:
            print(f"Final Hand: {player_hand}, current score: {get_score(True)}\n"
                  f"Dealers cards: {comp_hand}, Final Score: {get_score(False)}\n"
                  f"your hand is a bust, you LOSE!")
            play()

        hit_or_pass = input("Type y to draw another card, type 'n' to pass: ").lower()
        if hit_or_pass == 'y':
            add_card()
        else:
            player_score = get_score(True)
            comp_score = get_score(False)
            while comp_score < 17:
                comp_hand.append(cards[random.randint(0, len(cards) - 1)])
                comp_score = get_score(False)

            if comp_score == 21 and len(comp_hand) == 2:
                print(f"Final Hand: {player_hand}, Final score: {player_score}\n"
                      f"Dealers cards: {comp_hand}, Final Score: 0 \n"
                      f"The Dealers has Blackjack, you LOSE!")
                play()
            elif comp_score <= 21 and comp_score > player_score:
                print(f"Final Hand: {player_hand}, Final score: {player_score}\n"
                      f"Dealers cards: {comp_hand}, Final Score: {comp_score}\n"
                      f"The Dealers hand is better, you LOSE!")
                play()
            elif player_score == 21 and len(player_hand) == 2:
                print(f"Final Hand: {player_hand}, Final score: 0\n"
                      f"Dealers cards: {comp_hand}, Final Score: {comp_score}\n"
                      f"Blackjack! you Win!!")
                play()
            else:
                print(f"Final Hand: {player_hand}, Final score: {player_score}\n"
                      f"Dealers cards: {comp_hand}, Final Score: {comp_score}\n"
                      f"congrats, you Win!")
                play()

play()
