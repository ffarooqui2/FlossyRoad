from turtle import Turtle


class Field(Turtle):
    def __init__(self):
        super().__init__()
        self.pensize(3)
        for i in range(255, -280, -30):
            self.penup()
            self.goto(300, i)
            self.pendown()
            self.goto(-300, i)
