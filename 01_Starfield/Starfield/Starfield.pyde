from Star import *

stars = []
speed = 0

def setup():
  size(600, 600)
  for i in range(0,200):
    stars[i] = Star()
  
def draw():
  speed = map(mouseX, 0, width, 0, 50)

  background(0)
  translate(width/2, height/2);
  for star in stars:
    star.update();
    star.show();
