import os


auction_data = []

def start_auction(auction_data):
    auction_continue = True
    while auction_continue:
        new_bid = {}
        new_bid["name"] = input("What is the name of the bidder?: ")
        new_bid["bid"]= int(input("What is the bid ammount?: "))
        auction_data.append(new_bid)
        more_bidders = input(("Are the more bidders? (yes/no): "))
        if more_bidders == "no": auction_continue = False
        os.system('cls' if os.name == 'nt' else 'clear')
    return auction_data

def calculate_winner(auction_data):
    max_bid = 0
    for auction_record in auction_data:
        if auction_record["bid"] > max_bid: 
            max_bid = auction_record["bid"]
            winner_bid = auction_record["name"]
    return winner_bid

auction_data = start_auction(auction_data)
print(f"Winer is {calculate_winner(auction_data)}")