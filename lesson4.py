from turtle import Turtle, Screen, colormode
from random import randint

colormode(255)

bobby = Turtle()
bobby.shape('turtle')
bobby.color("dark green")
bobby.pensize(4)
bobby.left(90)

scr = Screen()

def forward():
    bobby.forward(15)

def back():
    bobby.backward(15)

def left():
    bobby.left(90)

def right():
    bobby.right(90)


def draw_square(side):
    for i in range(4):
        bobby.forward(side)
        bobby.right(90)


def draw_triangle(side):
    for i in range(3):
        bobby.forward(side)
        bobby.left(120)


def get_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b

# def draw_flower(petal_count=None):
#     if not petal_count:
#         petal_count = randint(3,12)
#     angle = 360/int(petal_count)
#     bobby.pencolor("green")
#     bobby.forward(200)
#     bobby.pencolor(get_color())
#     for i in range(petal_count):
#         bobby.circle(30)
#         bobby.left(angle)
#     bobby.penup()
#     bobby.back(200)
#     bobby.pendown()
#
# def draw_field():
#     for f in range(5):
#         draw_flower()
#         bobby.penup()
#         bobby.left(90)
#         bobby.forward(140)
#         bobby.right(90)
#         bobby.pendown()

scr.listen()
bobby.penup()
bobby.goto(250, -200)
bobby.pendown()

# bobby.pencolor(get_color())
# draw_square(200)
# bobby.pencolor(get_color())
# draw_triangle(200)
# bobby.circle(150)

# scr.onkey(draw_flower, 'q')
# scr.onkey(forward, 'f')
# scr.onkey(back, 'd')
# scr.onkey(left, 'j')
# scr.onkey(right, 'k')

scr.exitonclick()