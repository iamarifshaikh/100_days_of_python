from art import word, image

print(image)
one = int(input("Enter the number 1: "))
two = int(input("Enter the number 2: "))
operation = input(f"Enter the operation you want to do with the numbers: ")


def calculate():
    if operation == "+":
        print(
            "The solution for "
            + str(one)
            + " and "
            + str(two)
            + " is "
            + str(one + two)
        )
    elif operation == "-":
        print(
            "The solution for "
            + str(one)
            + " and "
            + str(two)
            + " is "
            + str(one - two)
        )
    elif operation == "*":
        print(
            "The solution for "
            + str(one)
            + " and "
            + str(two)
            + " is "
            + str(one * two)
        )
    elif operation == "/":
        print(
            "The solution for "
            + str(one)
            + " and "
            + str(two)
            + " is "
            + str(one / two)
        )
    else:
        print("Something went wrong!")


calculate()
