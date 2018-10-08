class Box():
    pos = PVector(0, 0, 0)
    size = 0
    
    def __init__(self, x, y, z, size):
        self.pos = PVector(x, y, z)
        self.size = size
        
    def show(self):
        pushMatrix()
        translate(self.pos.x, self.pos.y, self.pos.z)
        box(self.size)
        popMatrix()
        
    def generate(self):
        boxes = []
        for x in range(-1,2):
            for y in range(-1,2):
                for z in range(-1,2):
                    sum = abs(x) + abs(y) + abs(z)
                    newSize = self.size/3
                    if sum > 1:
                        boxes.append(Box(self.pos.x + (newSize*x), self.pos.y + (newSize*y), self.pos.z + (newSize*z), newSize))  
        return boxes
            
