import random
from Vector import Vector
from Bomb import Bomb
from EMP import EMP
from NailBomb import NailBomb
from PeaShooter import PeaShooter
from Shotgun import Shotgun

class Weapon:
    def __init__(self, width, height):
        self.type = random.choice([PeaShooter(), Shotgun()])
        #self.type = random.choice([PeaShooter(), Bomb(), EMP(), NailBomb()])
        self.pos = Vector(random.randrange(10, width-10), random.randrange(10, width-10))
        self.pickUp = False
        self.radius = 9

    def draw(self, canvas):
       canvas.draw_circle(self.pos.getP(), 9, 1, 'Green', 'Green') 

    def getValue(self):
        return self.type

    def draw(self, canvas):
         canvas.draw_circle(self.pos.getP(), 9, 1, 'Blue', 'Blue')

    def isPickedUp(self):
        return self.pickedUp

    def getPos(self):
        return self.pos

    def getRadius(self):
        return self.radius

    def pickUp(self):
        self.pickedUp = True

    def getType(self):
        return 'Weapon'

    def getPower(self):
        return None
