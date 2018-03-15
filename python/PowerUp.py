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
        #self.value = random.choice([God(), Shield()])
        self.value = Shield()
        self.pos = Vector(random.randrange(10, width-10), random.randrange(10, height-10))
        self.radius = 9
        self.sprite = simplegui.load_image("https://i.imgur.com/cVbBit3.png")

    def draw(self, canvas):
        canvas.draw_image(self.sprite, (16, 16), (self.sprite.get_width(), self.sprite.get_height()),
                          self.pos.getP(), (self.radius * 2, self.radius * 2))
        #canvas.draw_circle(self.pos.getP(), self.radius, 1, 'Red', 'Red')

    def getPos(self):
        return self.pos

    def getRadius(self):
        return self.radius

    def getType(self):
        return 'PowerUp'

    def getValue(self):
        return self.value
