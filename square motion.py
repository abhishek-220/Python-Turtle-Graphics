import turtle

# graphic screen function
wn = turtle.Screen()
wn.bgcolor("green")
wn.setup(800, 800)
wn.tracer(0)

# turtle functions
t = turtle.Turtle()
t.pensize(2)
t.pencolor("cyan")
t.hideturtle()
t.penup()
t.goto(-400, 30)
t.pendown()

# function to draw square
def square():
    t.begin_fill()
    t.fillcolor("cyan")
    for i in range(4):
        t.forward(60)
        t.right(90)

    t.end_fill()

if __name__ == "__main__":
    # infinte loop
    while True:
        t.clear()
        # calling square function
        square()
        # screen updation
        wn.update()

        t.forward(0.1)

