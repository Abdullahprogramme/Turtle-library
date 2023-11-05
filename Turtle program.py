import turtle as t
import math as m
window = t.Screen()
window.bgcolor(50 / 255, 50 / 255, 50 / 255)
cur = t.Turtle()
cur.shape("circle")
cur.color("Maroon", "Cyan")
cur.speed(50)
radius = 100


def circle():
    for i in range(360):

        y = radius * m.sin(m.radians(i))
        cur.begin_fill()
        cur.goto(i - radius, y)
        cur.end_fill()
        window.update()
        cur.pendown()

cur.penup()
circle()
cur.done()
    