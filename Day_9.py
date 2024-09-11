from art import logo

print(logo)

continue_bidding = "yes"
bidders_dict = {}

while continue_bidding == "yes":
    bidder_name = input("What is your name?: ")
    bid_amount = input("What is your bid?: $")
    bidders_dict[bidder_name] = bid_amount
    continue_bidding = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if continue_bidding == "yes":
        print("\n" * 100)

for bidder, bid in bidders_dict.items():
    if bid == max(bidders_dict.values()):
        print(f"The winner is {bidder} with a bid of ${bid}")
