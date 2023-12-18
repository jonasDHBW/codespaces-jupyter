import turtle

skk = turtle.Turtle()

skk.left(60)
skk.forward(20)

for i in range(6):
    skk.forward(30)
    skk.right(30)

skk.forward(30)
skk.right(20)
skk.forward(140)
skk.right(80)
skk.forward(140)
skk.right(20)

for i in range(6):
    skk.forward(30)
    skk.right(30)

skk.left(5)
skk.forward(55)

turtle.done()