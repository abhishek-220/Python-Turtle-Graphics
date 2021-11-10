import turtle
from turtle import *
#to create simple robot

t = turtle.Turtle()
t.speed(0)

wn = turtle.Screen()
wn.bgcolor('black')

t.color('blue')
t.goto(0, 0)
t.speed(3)

# for calling rest of the function
def body():
    head()
    chest()
    arms()
    inner()
    leg()

# for drawing the head
def head():
    t.begin_fill()
    t.fillcolor('yellow')
    t.circle(30)
    t.end_fill()

    t.begin_fill()
    t.fillcolor('silver')
    t.circle(24)
    t.end_fill()

# for drawing the body of the robot
def chest():
    t.begin_fill()
    t.fillcolor('yellow')
    t.forward(60)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(60)
    t.end_fill()

# for drawing the arms of the robot
def arms():
    t.up()
    t.goto(60, -35)
    t.down()
    t.pensize(2)
    t.right(45)
    t.forward(60)
    t.right(20)
    t.forward(50)

    t.penup()
    t.goto(-60, -35)
    t.pendown()
    t.right(65)
    t.forward(60)
    t.left(20)
    t.forward(50)

def inner():
    t.right(70)
    t.right(180)

    t.penup()
    t.goto(0, -20)
    t.pendown()
    t.begin_fill()
    t.fillcolor('silver')
    t.forward(40)
    t.right(90)
    t.forward(80)
    t.right(90)
    t.forward(80)
    t.right(90)
    t.forward(80)
    t.right(90)
    t.forward(40)
    t.end_fill()

# for drawing the legs of the robot
def leg():
    t.penup()
    t.goto(0, 0)
    t.goto(30, -120)
    t.pendown()
    t.width(4)

    t.right(60)
    t.forward(70)
    t.right(20)
    t.forward(60)

    t.penup()
    t.goto(-30, -120)
    t.pendown()

    t.right(40)
    t.forward(70)
    t.left(20)
    t.forward(60)

t.hideturtle()

if __name__ == '__main__':
    body()
    mainloop()
