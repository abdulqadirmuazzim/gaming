import turtle

b = turtle.Turtle()
b.speed(0)
turtle.bgcolor("black")
c = 0
li = ["red", "blue", "yellow", "coral", "cyan", "linen"]

for a in range(120):
    b.color("steelblue")
    b.forward(c)
    b.left(60)
    b.circle(100, a)
    b.backward(1)
    b.right(1)
    c += 1


turtle.mainloop()
