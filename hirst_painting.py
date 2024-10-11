import turtle as t
from turtle import Screen
import random
import colorgram

tim = t.Turtle()
t.colormode(255) # either 1 or 255; 1 includes rgb in the scale from
# 0 to 1 and the 255 includes the common rgb range from 0 to 255
screen = Screen()

tim.speed("fastest")

colors = colorgram.extract('damien hirst colours 45.webp', 45)
print(colors)

rgb_colors_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors_list.append(new_color)

print(rgb_colors_list)


def random_color():
    global colour
    colour = random.choice(rgb_colors_list)
    return colour

tim.penup()
tim.setposition(-200,-200)
tim.pendown()
tim.hideturtle()

for row_circles in range(10): # for loop of each row; paint 10 filled circles of size 20 at a
    # distance of 50 from each other and placing the turtle at the start of the next row on top (10 rows)
    for circles in range(10):
        tim.setheading(0)
        random_color()
        tim.fillcolor(colour)
        tim.begin_fill()
        tim.circle(20) # circle of size 20
        tim.end_fill()
        tim.penup()
        tim.forward(50)
        tim.pendown()

    # finished line, pen up to move to next row on top to perform another 10 circles
    tim.penup()
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500) # 10x50=450 to go back to starting line on top of previously drawn
    tim.pendown()


screen.exitonclick()