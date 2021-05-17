import turtle as t
import random


turtle = t.Turtle()
turtle.speed(0)
turtle.hideturtle()
colors = [(201, 164, 112), (152, 75, 50), (221, 201, 138), (57, 95, 126), (170, 152, 44), (138, 31, 20), (135, 163, 183), (196, 94, 75), (49, 121, 88), (143, 177, 149), (95, 75, 77), (76, 39, 32), (164, 146, 157), (16, 98, 71), (232, 176, 165), (54, 46, 48), (32, 61, 76), (22, 83, 89), (182, 204, 176), (141, 22, 25), (86, 147, 127), (45, 66, 85), (8, 68, 53), (177, 94, 97), (222, 177, 182), (109, 128, 151)]
t.colormode(255)
x = -225
y = -225
turtle.penup()
turtle.setpos(x, y)
dot_num = 1
is_on = True

while is_on:
    turtle.dot(20, random.choice(colors))
    if dot_num % 100 == 0:
        is_on = False
    elif dot_num % 20 == 0:
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)
        turtle.dot(20, random.choice(colors))
        dot_num += 1
    elif dot_num % 10 == 0:
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)
        turtle.dot(20, random.choice(colors))
        dot_num += 1
    turtle.forward(50)
    dot_num += 1





screen = t.Screen()
screen.exitonclick()