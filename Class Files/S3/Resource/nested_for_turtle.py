import turtle
turtle.colormode(255)
turtle.getscreen()
t = turtle.Turtle()
t.speed('fastest')


r = 0
g = 0
b = 0
for i in range(100):
    if r <= 249 and g<=253 and b<= 251:
        r += 2
        g += 2
        g = int(g)
        b += 2
        t.pencolor((r,g,b))
    else:
        r -= 2
        g -= 2
        g = int(g)
        b -= 4
        t.pencolor((r,g,b))
    for j in range(4):
        t.fd(200)
        t.lt(90)


    t.lt(3.6)

