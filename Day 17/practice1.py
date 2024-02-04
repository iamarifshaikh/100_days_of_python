from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Anime Name", "Type"]
table.align = "l"

while True:
    name = input(
        "Enter the anime name (or 'quit' to quit, 'show' to display the table): "
    )
    if name == "quit":
        break
    elif name == "show":
        print(table)
        continue

    anime_type = input("Enter the type of anime: ")

    # Add the user input as a new row in the table
    table.add_row([name, anime_type])

    # Print the table after each row is added
    print(table)
