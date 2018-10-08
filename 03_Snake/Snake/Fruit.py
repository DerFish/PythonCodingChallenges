class Fruit():
    def __init__(self):
        self.pos = PVector(220, 220)
        self.size = 20
        
    def show(self):
        fill(255, 0, 0)
        rect(self.pos.x, self.pos.y, self.size, self.size)
        
    def newPos(self):
        self.pos = PVector(floor(random(0, 25))* 20, floor(random(0, 25))* 20) 
