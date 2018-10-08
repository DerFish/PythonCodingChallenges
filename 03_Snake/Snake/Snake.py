class Snake:
    def __init__(self):
        self.pos = PVector(40, 40)
        self.xAcc = 1
        self.yAcc = 0
        self.size = 20
        self.tail = []
        
    def show(self):
        fill(255)
        rect(self.pos.x, self.pos.y, self.size, self.size)
        
        for sn in self.tail:
            rect(sn.pos.x, sn.pos.y, sn.size, sn.size)
        
    def update(self):
        for sn in range(len(self.tail)-1, 0, -1):
            self.tail[sn].pos.x = self.tail[sn-1].pos.x
            self.tail[sn].pos.y = self.tail[sn-1].pos.y
                            
        self.tail[0].pos.x = self.pos.x
        self.tail[0].pos.y = self.pos.y
            
        self.pos.x += self.xAcc * self.size
        self.pos.y += self.yAcc * self.size
        
    def changeDirection(self, x, y):
        self.xAcc = x
        self.yAcc = y
        
    def eatenFruit(self, fruitX, fruitY):
        if self.pos.x == fruitX and self.pos.y == fruitY:
            sn = Snake()
            sn.pos.x = self.tail[-1].pos.x + (self.xAcc * self.size)
            sn.pos.y = self.tail[-1].pos.y + (self.yAcc * self.size)
            self.tail.append(sn)
            return True
        else:
            return False
