import os

def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
    
def start():
    print()
start()
play = input("Start Game? y/n: ")
    
def highest_bids(record):
    highest_bid = 0
    winner = ""
    
    for bidder in record:
        bid_amt = record[bidder]
        if int(bid_amt) > int(highest_bid):
            highest_bid = bid_amt
            winner = bidder
    print(f"The highest bid belongs to {winner} with an amount of ${highest_bid}.")

bids = {}
end_bid = False

if play == 'y':
    start()
    while not end_bid:
        name = input("What is your name? ")
        bid_price = input("What is your bid amount? $")
        bids[name] = bid_price
        
        user = input("Are there other users who want to bid? y/n: ")
        if user == 'n':
            end_bid = True
            highest_bids(bids)
        elif user == 'y':
            clear()
else:
    print("Thank you, See you again!")
