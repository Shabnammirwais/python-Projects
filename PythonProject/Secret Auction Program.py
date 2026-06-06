logo = r"""
  ____                  _            _             
 / ___|  ___ _ ____   _(_) ___ ___  | |_ ___  _ __ 
 \___ \ / _ \ '__\ \ / / |/ __/ _ \ | __/ _ \| '__|
  ___) |  __/ |   \ V /| | (_|  __/ | || (_) | |   
 |____/ \___|_|    \_/ |_|\___\___|  \__\___/|_|   
"""

print(logo)

print("Welcome to the secret auction program!")

bids = {}

should_continue = True
while should_continue:
    name = input("What is your name?: ")
    bid_amount = int(input("What's your bid?: "))
    other_bidder = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    bids[name] = bid_amount

    if other_bidder == "no":
        winner = max(bids, key=bids.get)
        winner_amount = bids[winner]
        print(f"The winner is {winner} with a bid of {winner_amount}")
        should_continue = False
