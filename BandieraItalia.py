import turtle
turtle.pensize(2)
turtle.speed(3)
colori=["red","white","green"]

x=0
def quadrato(color,latoC,latoL):
    turtle.color(color)
    turtle.forward(latoC)
    turtle.left(90)
    turtle.forward(latoL)
    turtle.left(90)
    turtle.forward(latoC)
    turtle.left(90)
    turtle.forward(latoL)
    turtle.left(90)
   
for color in colori:
    turtle.begin_fill()
    quadrato(color,100,200)
    turtle.end_fill()
    x+=100
    turtle.goto(x,0)
    
x=0
turtle.goto(x,0)
quadrato("black",300,200)
turtle.done()