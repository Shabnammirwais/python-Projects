# from turtle import Turtle, Screen
# t = Turtle()
# t.shape("turtle")
# t.color("blue")
# # Draw a dashed line
# for _ in range(15): # Adjust the range for longer or shorter lines
#    t.forward(10) # Draw a segment of the line
#    t.penup() # Lift the pen to create a gap
#    t.forward(10) # Move forward without drawing
#    t.pendown() # Put the pen down to resume drawing
#
# # Exit on click
# screen = Screen()
# screen.exitonclick()
#

# import colorgram
# colors = colorgram.extract('image.jpg', 5)
#
# print(colors)

# from turtle import Turtle, Screen
#
# tim = Turtle()
# screen = Screen()
#
# def move_forward():
#     tim.forward(10)
# def move_backward():
#     tim.backward(10)
# def turn_left():
#     tim.left(10)
# def turn_right():
#     tim.right(-10)
# def clear_all():
#     tim.clear()
#
# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="d", fun= turn_right)
# screen.onkey(key="c", fun=clear_all)
# screen.exitonclick()


################################################################  TURTL RACE PROJECT ###########################################################
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width = 500, height = 500)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")
color = ["red", "yellow", "green", "blue", "purple", "orange"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(0, 6):
  new_turtle = Turtle(shape="turtle")
  new_turtle.penup()
  new_turtle.color(color[turtle_index])
  new_turtle.goto(x=-230, y=y_position[turtle_index])
  all_turtle.append(new_turtle)

if user_bet:
  is_race_on = True

while is_race_on:

  for turtle in all_turtle:
    if turtle.xcor() > 230:
      is_race_on = False
      winner_color = turtle.pencolor()
      if user_bet == winner_color:
        print(f"You won!. The winner Color is {winner_color}")
      else:
        print(f"You lost :( The winner Color is {winner_color}")


  for turtle in all_turtle:
    random_distance = random.randint(0,10)
    turtle.forward(random_distance)


screen.exitonclick()