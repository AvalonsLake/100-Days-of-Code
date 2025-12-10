import art

print(art.logo)

bidding = True
bidders = {}
winner = {
    "winner": ["placeholder", 0]
}

def determine_highest_bidder():
    for key in bidders:
        if winner["winner"][1] < bidders[key][1]:
            winner["winner"][0] = bidders[key][0]
            winner["winner"][1] = bidders[key][1]

    print(f"The winner is {winner['winner'][0]} with a bid of ${winner['winner'][1]}")


while bidding:
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))

    bidders[name] = [name, bid]

    other_bidders = input("Are there other bidders? Type 'yes' or 'no' ").lower()

    print("\n" * 25)
    if other_bidders == "no":
        bidding = False
        determine_highest_bidder()
