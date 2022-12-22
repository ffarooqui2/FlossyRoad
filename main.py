import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from field import Field

# Screen setup
screen = Screen()
screen.title("Flossy Road")
screen.setup(width=600, height=600)
screen.tracer(0)

# Other objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
field = Field()

# Controls keyboard inputs
screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True  # Flag that tells whether our game should be running

# Game loop
while game_is_on:

    # Controls how much the screen updates
    time.sleep(0.03)
    screen.update()

    # Checks weather the player has passed the level
    if player.ycor() > 280:
        player.reset_position()
        scoreboard.increase_score()
        car_manager.increase_speed()

    # Simulate cars
    car_manager.generate_car()
    car_manager.move_cars()

    # Removes cars from the list of cars if they pass the border
    # This will also conserve memory
    for car in car_manager.all_cars:
        if car.xcor() < -320:
            car.hideturtle()
            car_manager.all_cars.remove(car)

    # Detect collision between a car and the player
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

# Print game over to screen
game_over_sign = Turtle()
game_over_sign.penup()
game_over_sign.goto(0, 260)
game_over_sign.color("red")
game_over_sign.write("GAME OVER", align="center", font=("Copperplate", 30, "bold"))

# print(len(car_manager.all_cars))

screen.exitonclick()
