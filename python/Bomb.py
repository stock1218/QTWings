try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Vector import Vector
from ExplosiveBomb import ExplosiveBomb
from NailBomb import NailBomb
from EMP import EMP
import random

class Bomb:

    def __init__(self, width, height):
        self.value = random.choice([ExplosiveBomb(), NailBomb(), EMP()])
        self.pos = Vector(random.randrange(10, width-10), random.randrange(10, height-10))
        self.radius = 9
        self.sprite = simplegui.load_image("https://i.imgur.com/cxXIRXF.png")

    def draw(self, canvas):
        canvas.draw_image(self.sprite, (16, 16), (self.sprite.get_width(), self.sprite.get_height()),
                          self.pos.getP(), (self.radius * 2, self.radius * 2))
        # canvas.draw_circle(self.pos.getP(), 9, 1, 'Green', 'Green')

    def getValue(self):
        return self.type

    def getPos(self):
        return self.pos

    def getRadius(self):
        return self.radius

    def getType(self):
        return 'Bomb'

    def getValue(self):
        return self.value
