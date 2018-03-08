import random
from Bullet import Bullet
from Bomb import Bomb
from EMP import EMP
from NailBomb import NailBomb
class Weapon:
    def __init__(self):
        self.type = random.choice([Bullet(), Bomb(), EMP(), NailBomb()])

    def getWeapon(self):
        return self.type
