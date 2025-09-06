from replit import clear
import art


print(art.logo)
print("Welcome to the secret auction program")
program_run = True
note_bid = {}


def bid_calculation(dict_bid, auction=0, win_name=""):
    for key, value in dict_bid.items():
        if value > auction:
            auction = value
            win_name = ""
            win_name += key
    print(f"The winner is {win_name} with bid ${auction}")


while program_run:
    name = input("What is your name: ")
    bid = int(input("What's your bid: $"))
    note_bid[name] = bid
    next_person = input("Are there any other bidders: type 'yes' or 'no'")
    if next_person.lower() == 'no':
        bid_calculation(dict_bid=note_bid)
        program_run = False
    elif next_person.lower() == 'yes':
        print("\n"*100)