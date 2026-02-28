bids = {}
biggest = 0

print("**Welcome to the Python Blind Auction!**\n\n")

while True:
    name = input("What's your name? ")
    bid = float(input("What's your bid? $"))
    bids.update({name:bid})

    any_more = input("There's another bid? (yes/no): ")

    if any_more.lower() == "no": break

    print("\n\n")

for key in bids:

    if bids[key] > biggest:
        biggest = bids[key]
        name = key


print(f"The winner is {name} with a bid of ${biggest}")