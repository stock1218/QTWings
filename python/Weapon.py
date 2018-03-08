import random
from Bomb import Bomb
from EMP import EMP
from NailBomb import NailBomb
from PeaShooter import PeaShooter
class Weapon:
    def __init__(self):
        self.type = random.choice([PeaShooter(), Bomb(), EMP(), NailBomb()])

    def getWeapon(self):
        return self.type
