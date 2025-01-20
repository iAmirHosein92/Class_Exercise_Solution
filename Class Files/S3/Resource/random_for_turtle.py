import turtle
from random import randint
turtle.colormode(255)
turtle.getscreen()
t = turtle.Turtle()
t.speed('fastest')



for i in range(100):
    r = randint(0,400)
    t.fd(r)
    t.bk(r)
    t.lt(3.6)

