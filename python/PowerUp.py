try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
 

from Vector import Vector 
import random

class PowerUp:
    
    def __init__(self, width, height):
        """Construct PowerUp"""
        self.type = random.choice(['God Mode', 'Shield'])
        self.pos = Vector(random.randrange(10, width-10), random.randrange(10, height-10))
        self.radius = 9 

    def draw(self, canvas):
        canvas.draw_circle((self.pos.x, self.pos.y), self.radius, 1, 'Red', 'Red') 

    def getPos(self):
        return self.pos

    def getRadius(self):
        return self.radius
