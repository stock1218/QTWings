try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Box import Box
from Vector import Vector
from random import randrange

class Obstacle:

    def __init__(self, width, height):
        self.obstacles = []
        for i in range(10):
            size = randrange(10,50)
            self.obstacles.append(Box(
                Vector(randrange(0, width), randrange(0, height)), 
                size,
                size))

    def getObstacles(self):
        return self.obstacles

    def draw(self, canvas):
        for i in self.obstacles:
            canvas.draw_polygon(i.points, i.thickness, 'Blue', 'White') 
            #i.draw(canvas) 
