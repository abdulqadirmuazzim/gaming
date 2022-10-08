import turtle
import colorsys as ss

b = turtle.Turtle()
b.speed(-2)
turtle.bgcolor("black")
c = 0
li = ["red", "blue", "yellow", "coral", "cyan", "linen"]

# for a in range(120):
#     b.color("steelblue")
#     b.forward(c)
#     b.left(60)
#     b.circle(100, a)
#     b.backward(1)
#     b.right(1)
#     c += 1


# turtle.mainloop()

class method():
    def __init__(self):
        self.col = ["red", "blue", "yellow", "coral", "cyan", "linen"]
        self.uni = ss.hsv_to_rgb(13, 151, 142)

    def draw(self):
        b.penup()
        b.goto(20, 0)
        b.pendown()
        for num in range(60):
            b.color(self.col[1])
            for nun in range(6):
                # b.begin_fill()
                b.forward(100)
                b.circle(20, 60.0)
                # b.end_fill()
            b.color(self.col[4])
            b.circle(50, 6)


met = method()
met.draw()
