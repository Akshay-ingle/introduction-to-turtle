import turtle
turtle.screen().bgcolor('orange')
turtle.screen().setup(300,400)
pg=turtle.Turtle()
ns=6
sl=70
ag=360.0/ns

for i in range(ns):
    pg.forward(sl)
    pg.right(ag)
turtle.done  