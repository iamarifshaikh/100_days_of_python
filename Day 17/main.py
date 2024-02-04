from turtle import Turtle, Screen
from prettytable import PrettyTable

# arif = Turtle()
# arif.shape("turtle")
# print(arif)
# myscreen = Screen()
# myscreen.exitonclick()
# print(myscreen.canvheight)
table = PrettyTable()
table.add_column("Anime Name", ["Attack On Titan", "Jujutu Kaisen", "Demon Slayer"])
table.add_column("Anime Type", ["Action", "Action", "Action"])
print(table)
