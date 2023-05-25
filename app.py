import turtle as t
import colorsys as ss
import time
import random as rn

t.bgcolor("black")

li = [t.Turtle(), t.Turtle()]
f = li[0]
s = li[1]

for i in li:
    i.speed(0)
    i.width(.5)
    i.shape("arrow")
    i.color("white", "black")

f.pu()
f.bk(200)
f.pd()

for a in range(4):
    for b in range(80):
        f.fd(5)
        s.color(ss.hsv_to_rgb(b/80, 0.787, 1))
        s.goto(f.pos())
        s.pu()
        s.goto(0, 0)
        s.pd()
    f.lt(90)


time.sleep(10)
