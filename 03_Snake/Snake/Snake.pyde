from Snake import *
from Fruit import *

s = Snake()
f = Fruit()

def setup():
    global s
    size(500, 500)
    frameRate(6)
    sn = Snake()
    sn.pos.x = 20
    sn.pos.y = 40
    s.tail.append(sn)
    sn2 = Snake()
    sn2.pos.x = 0
    sn2.pos.y = 40
    s.tail.append(sn2)

def draw():
    background(0)
    s.show()
    s.update()
    if s.eatenFruit(f.pos.x, f.pos.y):
        f.newPos()
    f.show()
    
def keyPressed():
    if keyCode == 38:
        s.changeDirection(0, -1)
    elif keyCode == 37:
        s.changeDirection(-1, 0)
    elif keyCode == 40:
        s.changeDirection(0, 1)
    elif keyCode == 39:
        s.changeDirection(1, 0)
