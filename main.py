import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program.")
bidders = {}
def add_bidder(name, bid):
    bidders[name] = bid
def find_highest_bidder(bidders):
  if len(bidders) == 0:
    print("There are no bidders.")
    return
  highest_bid=0
  highest_bidder=""
  for key in bidders:
    if bidders[key] >highest_bid:
      highest_bid = bidders[key]
      highest_bidder = key
  print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")  
# more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
bidding_finished=False
while not bidding_finished:
  name=input("what is your name?: ")
  bid=int(input("what is your bid?: $"))
  add_bidder(name, bid)
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if should_continue== "no":
    bidding_finished=True
    find_highest_bidder(bidders)
  else:
    def clear_console():
      os.system('cls' if os.name == 'nt' else 'clear')

    # Call the function to clear the console
    clear_console()



 
  
   
  
  
  
