bids = {}
biddingFinished = False

def highestBidding(bidders):
  startingBid = 0
  winner = ""

  for bidder in bidders:
    bidAmount = bidders[bidder]
    if bidAmount > startingBid:
      startingBid = bidAmount
      winner = bidder
  print(f"The winner is {winner} with a bid amount of ${bidAmount}")


while not biddingFinished:
    name = input("What is your name?\n")
    price = int(input("How much would you like to bid?\n$"))
    bids[name] = price
    anotherBidder = input("If there are any other bidders, type 'YES'; otherwise, type 'NO'\n")
    if anotherBidder.lower() == "no":
        biddingFinished = True
        highestBidding(bids)