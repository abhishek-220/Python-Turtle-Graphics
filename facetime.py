import turtle
from turtle import *

t = turtle.Turtle()
t.pencolor('white')
t.pensize(2)

wn = turtle.Screen()
wn.setup(800, 800)
wn.bgcolor('black')

def ears():
    t.penup()
    t.goto(-60, 113)
    t.pendown()
    t.begin_fill()
    t.fillcolor('white')
    t.circle(20)
    t.penup()
    t.goto(60, 113)
    t.pendown()
    t.circle(20)
    t.end_fill()

def inner_ears():
    t.penup()
    t.goto(-63, 115)
    t.pendown()
    t.begin_fill()
    t.fillcolor('black')
    t.circle(14)
    t.penup()
    t.goto(63, 115)
    t.pendown()
    t.circle(14)
    t.end_fill()


def eyes():
    t.penup()
    t.goto(-24,75)
    t.pendown()
    t.begin_fill()
    t.fillcolor('white')
    t.circle(8)
    t.penup()
    t.goto(24, 75)
    t.pendown()
    t.circle(8)
    t.end_fill()

def inner_eyes():
    t.penup()
    t.goto(-22, 75)
    t.pendown()
    t.begin_fill()
    t.fillcolor('black')
    t.circle(6)
    t.penup()
    t.goto(22, 75)
    t.pendown()
    t.circle(6)
    t.end_fill()

def face():
    t.penup()
    t.goto(0, -5)
    t.pendown()
    t.circle(70)

def mouth():
    t.penup()
    t.goto(-23, 45)
    t.pendown()
    t.right(90)
    t.circle(24, 180)

t.hideturtle()

if __name__ == "__main__":
    ears()
    inner_ears()
    eyes()
    inner_eyes()
    face()
    mouth()
    mainloop()