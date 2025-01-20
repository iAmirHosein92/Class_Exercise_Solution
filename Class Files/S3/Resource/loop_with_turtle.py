import turtle
turtle.colormode(255)
turtle.getscreen()
t = turtle.Turtle()
t.speed('fastest')
t.pencolor((41,41,253))

c = 0
for i in range(8):
    print(c)
    t.fd(100)
    t.lt(360/8)
    if c%2 == 1:
        t.pencolor((41,41,253))      
    else:
        t.pencolor((255,255,255))

    c += 1

