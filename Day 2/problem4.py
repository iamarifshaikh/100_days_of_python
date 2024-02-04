def tipCalculator(food:int,tip_percentage:float) -> float:
  tip = food * (tip_percentage / 100)
  print("The tip amount you need to pay is $",tip)

  total = tip + food
  print("The total amount you need to pay is $",total)

tipCalculator(200,2.5)
