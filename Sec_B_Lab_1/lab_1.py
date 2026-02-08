import turtle
import random
import time

screen = turtle.Screen()
screen.bgcolor("black")
screen.title('Turtle is fun!')

t = turtle.Turtle()
t.speed(0)
t.pensize(2)

palette = ['cyan', 'magenta', 'yellow', 'lime', 'orange', 'white', 'red', 'blue', 'green']

t.penup()
t.goto(0, 0)
t.pendown()

for i in range(200):
    t.pencolor(random.choice(palette))
    t.forward(i * 2)
    t.right(91)

t.penup()
t.goto(-180, -250)
t.pencolor("white")
t.write("Python is fun!", font=("Arial", 16, "normal"))

t.hideturtle()
time.sleep(5)

turtle.done()