import random
from Vector import Vector
from Bomb import Bomb
from EMP import EMP
from NailBomb import NailBomb
from PeaShooter import PeaShooter
from Shotgun import Shotgun

class Weapon:
    def __init__(self, width, height):
        self.value = random.choice([PeaShooter(), Shotgun()])
        #self.value = random.choice([PeaShooter(), Bomb(), EMP(), NailBomb()])
        self.pos = Vector(random.randrange(10, width-10), random.randrange(10, height-10))
        self.pickUp = False
        self.radius = 9

    def getValue(self):
        return self.value

    def draw(self, canvas):
         canvas.draw_circle(self.pos.getP(), 9, 1, 'Blue', 'Blue')

    def getPos(self):
        return self.pos

    def getRadius(self):
        return self.radius

    def getType(self):
        return 'Weapon'
