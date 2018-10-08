from Box import *

angle = 0.01
ownBox = []

def setup():
    global ownBox
    size(1000, 1000, P3D)
    angle = 0
    ownBox.append(Box(0, 0, 0, 500))
    
    
def draw():
    global angle
    global ownBox
    
    background(52)
    translate(height/2, width/2)
    rotateX(angle)
    rotateY(angle)
    lights()
    angle += 0.01
    for b in ownBox:
        b.show()
    
def mousePressed():
    global ownBox
    newBoxes = []
    for b in ownBox:
        newBoxes.extend(b.generate())
    ownBox = []
    ownBox.extend(newBoxes)
