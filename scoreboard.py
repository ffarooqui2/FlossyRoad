from turtle import Turtle
FONT = ("Copperplate", 20, "bold")


class Scoreboard (Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level_num = 1
        self.update_screen()

    def update_screen(self):
        self.clear()
        self.goto(-230, 260)
        self.write("Level: " + str(self.level_num), align="center", font=FONT)

    def increase_score(self):
        self.level_num = self.level_num + 1
        self.update_screen()
