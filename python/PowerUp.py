try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
 
from Shield import Shield
from Vector import Vector 
import random

class PowerUp:
    
    def __init__(self, width, height):
        """Construct PowerUp"""
        self.type = random.choice(['God Mode', 'Shield'])
        #if(self.type == 'Shield'):
        self.power = Shield()
        #else:
            #self.power = God()

        self.pos = Vector(random.randrange(10, width-10), random.randrange(10, height-10))
        self.radius = 9 

    def draw(self, canvas):
        canvas.draw_circle(self.pos.getP(), self.radius, 1, 'Red', 'Red') 

    def getPos(self):
        return self.pos

    def getRadius(self):
        return self.radius

    def getType(self):
        return 'PowerUp'

    def getValue(self):
        return self.power
