import random
import turtle
from turtle import Turtle, Screen
# from turtle import * (*: imports everything from the module, can be confusing and not used most of the time)
# import turtle (This will make it harder if we are using this module a lot
# (e.g. timmy = turtle.Turtle(), tom = turtle.Turtle()))
# import turtle as t (this will make it easy to write the code (e.g. timmy = t.Turtle(), tom = t.Turtle()))

# Installing Modules: from settings we can add and remove interpreters like prettyTable or heroes (pypi.org)
# Pycharm can detect the module that is not installed and gives a red lightbulb error,
# you can install the module by clicking on the red lightbulb and install module (see the example below)
# import heroes


timmy = Turtle()
screen = Screen()
timmy.shape("turtle")
timmy.color("DarkSlateGray")

# Challenge 1: Build a square with turtle
# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)

# Challenge 2: Draw a Dashed Line
# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# Challenge 3: Drawing Different Shapes
# from random import randint
#
# corners = 3
# screen.colormode(255)
# while corners != 10:
#     timmy.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
#     for _ in range(corners):
#         timmy.forward(100)
#         timmy.right(360/corners)
#     corners += 1

# Challenge 3: Drawing Different Shapes Teacher's Solution
# import random
#
# colours = ["gray", "aquamarine", "navy", "red", "medium slate blue", "medium violet red", "blue violet", "dark green"]
#
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     timmy.color(random.choice(colours))
#     draw_shape(shape_side_n)

# Challenge 4: Generate a Random Walk
# from random import randint, choice
#
# screen.colormode(255)
# timmy.pensize(15)
# timmy.speed("fastest")
# walk = 0
#
# while walk != 200:
#     timmy.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
#     left_or_right = [0, 1]
#     movement = choice(left_or_right)
#     if movement == 0:
#         timmy.left(90)
#     else:
#         timmy.right(90)
#     timmy.forward(50)
#
#     walk += 1

# Challenge 4: Generate a Random Walk Teacher's Solution
# import random
#
# colours = ["gray", "aquamarine", "navy", "red", "medium slate blue", "medium violet red", "blue violet", "dark green"]
# directions = [0, 90, 180, 270]
# timmy.pensize(15)
# timmy.speed("fastest")
#
# for _ in range(200):
#     timmy.color(random.choice(colours))
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))

# A Tuple is like an unchangeable (immutable) list with () instead of []
# turtle.colormode(255)
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
#
#
# directions = [0, 90, 180, 270]
# timmy.pensize(15)
# timmy.speed("fastest")
#
# for _ in range(200):
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))

# Challenge 5: Draw a Spirograph

# screen.colormode(255)
# timmy.speed("fastest")
# timmy.pensize(2)
# 
# for _ in range(72):
#     timmy.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     timmy.circle(100)
#     timmy.left(5)


# Challenge 5: Draw a Spirograph Teacher's Solution

# turtle.colormode(255)
# timmy.speed("fastest")
# timmy.pensize(2)
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
#
#
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         timmy.color(random_color())
#         timmy.circle(100)
#         timmy.setheading(timmy.heading() + size_of_gap)
#
#
# draw_spirograph(5)











# timmy.left(50)
# timmy.forward(50)
# timmy.right(80)
# timmy.forward(100)
# timmy.right(100)
# timmy.forward(180)
# timmy.right(90)
# timmy.forward(190)
# timmy.right(100)
# timmy.forward(100)
# timmy.right(80)
# timmy.forward(70)
# timmy.left(90)
# timmy.forward(20)



screen.exitonclick()
