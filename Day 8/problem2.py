def itIsPrimeNumberOrNot(number):
  isPrime = True
  for check in range(2, number):
    if number % check == 0:
      isPrime = False

  if isPrime:
    print(f"{number} is prime number")
  else:
    print(f"{number} is not a prime number")

itIsPrimeNumberOrNot(3)