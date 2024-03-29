import random
from Vector import Vector
from Bomb import Bomb
from EMP import EMP
from NailBomb import NailBomb
from PeaShooter import PeaShooter
from Shotgun import Shotgun
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Weapon:
    def __init__(self, width, height):
        self.value = random.choice([PeaShooter(20), Shotgun()])
        self.pos = Vector(random.randrange(10, width-10), random.randrange(10, height-10))
        self.pickUp = False
        self.radius = 9
        self.sprite = simplegui.load_image("https://i.imgur.com/qTEUqHV.png")

    def getValue(self):
        return self.value

    def draw(self, canvas):
        canvas.draw_image(self.sprite, (16, 16), (self.sprite.get_width(), self.sprite.get_height()), self.pos.getP(),
                          (self.radius * 2, self.radius * 2))
        # canvas.draw_circle(self.pos.getP(), 9, 1, 'Blue', 'Blue')

    def getPos(self):
        return self.pos

    def getRadius(self):
        return self.radius

    def getType(self):
        return 'Weapon'
